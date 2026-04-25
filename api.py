from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from database import get_db, engine
from models import DailyMetrics
from schemas import MetricsInput, MetricsResponse, DecisionResponse, ManualThresholds
from engines import EngineRuleAutomated, EngineRuleUserDefined
from analyzers import TrendAnalyzer

# Create tables
DailyMetrics.metadata.create_all(bind=engine)

app = FastAPI(title="Meta Ads Decision Engine API")


@app.get("/")
def home():
    return {"message": "Meta Ads Decision Engine API", "status": "running"}


@app.post("/metrics", response_model=MetricsResponse)
def add_metrics(data: MetricsInput, db: Session = Depends(get_db)):
    """Submit daily ad metrics"""
    ctr, cpc, roas = DailyMetrics.calculate_metrics(
        data.spend, data.impressions, data.clicks, data.revenue
    )
    metrics = DailyMetrics(
        spend=data.spend,
        clicks=data.clicks,
        impressions=data.impressions,
        revenue=data.revenue,
        ctr=ctr, cpc=cpc, roas=roas,
        date=data.date
    )
    db.add(metrics)
    db.commit()
    db.refresh(metrics)
    return metrics


@app.get("/metrics", response_model=list[MetricsResponse])
def get_all_metrics(db: Session = Depends(get_db)):
    """Get all stored metrics"""
    return db.query(DailyMetrics).all()


@app.post("/decision/auto", response_model=DecisionResponse)
def auto_decision(data: MetricsInput, db: Session = Depends(get_db)):
    """Get automated Scale/Hold/Stop decision"""
    ctr, cpc, roas = DailyMetrics.calculate_metrics(
        data.spend, data.impressions, data.clicks, data.revenue
    )
    engine = EngineRuleAutomated(ctr=ctr, cpc=cpc, roas=roas)
    return DecisionResponse(decision=engine.decision(), ctr=ctr, cpc=cpc, roas=roas)


@app.post("/decision/manual", response_model=DecisionResponse)
def manual_decision(data: MetricsInput, thresholds: ManualThresholds, db: Session = Depends(get_db)):
    """Get user defined decision"""
    ctr, cpc, roas = DailyMetrics.calculate_metrics(
        data.spend, data.impressions, data.clicks, data.revenue
    )
    engine = EngineRuleUserDefined(
        ctr=ctr, cpc=cpc, roas=roas,
        scale_ctr=thresholds.scale_ctr,
        scale_cpc=thresholds.scale_cpc,
        scale_roas=thresholds.scale_roas,
        stop_ctr=thresholds.stop_ctr,
        stop_cpc=thresholds.stop_cpc,
        stop_roas=thresholds.stop_roas
    )
    return DecisionResponse(decision=engine.decision(), ctr=ctr, cpc=cpc, roas=roas)


@app.get("/trend", response_model=dict)
def get_trend(db: Session = Depends(get_db)):
    """Get 3-day trend analysis"""
    metrics = db.query(DailyMetrics).order_by(DailyMetrics.date.desc()).limit(3).all()
    if len(metrics) < 3:
        raise HTTPException(status_code=400, detail="Need at least 3 days of data")
    
    days_data = [{"ctr": m.ctr, "cpc": m.cpc, "roas": m.roas} for m in reversed(metrics)]
    analyzer = TrendAnalyzer(days_data)
    return {"trend_decision": analyzer.decision()}