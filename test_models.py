from models import DailyMetrics

def test_ctr_calculation():
    m = DailyMetrics(100, 1000, 50, 200)
    assert m.ctr == 5.0

def test_zero_clicks_raises():
    try:
        DailyMetrics(100, 1000, 0, 200)
    except ValueError:
        pass

def test_cpc_calculation():
    m = DailyMetrics(100, 1000, 50, 200)
    assert m.cpc == 2.0