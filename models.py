from sqlalchemy import Column, Integer, Float, Date
from database import Base


class DailyMetrics(Base):
    """Database table for daily ad metrics"""
    __tablename__ = "daily_metrics"

    id = Column(Integer, primary_key=True, index=True)
    spend = Column(Float, nullable=False)
    clicks = Column(Integer, nullable=False)
    impressions = Column(Integer, nullable=False)
    revenue = Column(Float, nullable=False)
    ctr = Column(Float, nullable=False)
    cpc = Column(Float, nullable=False)
    roas = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    @staticmethod
    def calculate_metrics(spend: float, impressions: int, clicks: int, revenue: float):
        """Calculate CTR, CPC, ROAS from raw data"""
        if clicks == 0:
            raise ValueError("Clicks cannot be zero")
        if impressions == 0:
            raise ValueError("Impressions cannot be zero")
        if spend == 0:
            raise ValueError("Spend cannot be zero")
        
        ctr = (clicks / impressions) * 100
        cpc = spend / clicks
        roas = revenue / spend
        return ctr, cpc, roas