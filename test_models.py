from models import DailyMetrics

def test_ctr_calculation():
    ctr, cpc, roas = DailyMetrics.calculate_metrics(100, 1000, 50, 200)
    assert ctr == 5.0

def test_zero_clicks_raises():
    try:
        DailyMetrics.calculate_metrics(100, 1000, 0, 200)
        assert False
    except ValueError:
        pass

def test_cpc_calculation():
    ctr, cpc, roas = DailyMetrics.calculate_metrics(100, 1000, 50, 200)
    assert cpc == 2.0