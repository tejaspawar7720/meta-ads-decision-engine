from pydantic import BaseModel
from datetime import date


class MetricsInput(BaseModel):
    """Schema for daily ad metrics input"""
    spend: float
    clicks: int
    impressions: int
    revenue: float
    date: date


class MetricsResponse(BaseModel):
    """Schema for metrics response"""
    id: int
    spend: float
    clicks: int
    impressions: int
    revenue: float
    ctr: float
    cpc: float
    roas: float
    date: date

    class Config:
        from_attributes = True


class DecisionResponse(BaseModel):
    """Schema for decision response"""
    decision: str
    ctr: float
    cpc: float
    roas: float


class ManualThresholds(BaseModel):
    """Schema for user defined thresholds"""
    scale_ctr: float
    scale_cpc: float
    scale_roas: float
    stop_ctr: float
    stop_cpc: float
    stop_roas: float