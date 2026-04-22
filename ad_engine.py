class DailyMetrics:
    def __init__(self, spend, impression, clicks, revenue):
        if clicks == 0:
            raise ValueError("clicks can not be Zero / 0 ")
        if impression == 0:
            raise ValueError("Impressions Can not be Zero / 0")
        if spend == 0:
            raise ValueError()
        self.ctr = (clicks / impression) * 100
        self.cpc = spend / clicks
        self.roas = revenue / spend

class EngineRuleAutomated:
    def __init__(self, ctr, cpc, roas):
        self.ctr = ctr
        self.cpc = cpc
        self.roas = roas

    def decision(self):
        if self.ctr >= 1 and self.cpc <= 10 and self.roas >= 3:
            return "Scale..."
        elif self.ctr <= 0.70 and self.cpc >= 20 and self.roas <= 2:
            return "Stop..."
        else:
            return "Hold..."

class EngineRuleUserDefined:
    def __init__(self, ctr, cpc, roas, scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas):
        self.ctr = ctr
        self.cpc = cpc
        self.roas = roas
        self.scale_ctr = scale_ctr
        self.scale_cpc = scale_cpc
        self.scale_roas = scale_roas
        self.stop_ctr = stop_ctr
        self.stop_cpc = stop_cpc
        self.stop_roas = stop_roas

    def decision(self):
        if self.ctr >= self.scale_ctr and self.cpc <= self.scale_cpc and self.roas >= self.scale_roas:
            return "Scale..."
        elif self.ctr <= self.stop_ctr and self.cpc >= self.stop_cpc and self.roas <= self.stop_roas:
            return "Stop..."
        else:
            return "Hold..."

try:
    spend = float(input("Enter Total spend: $"))
    clicks = float(input("Enter Total Clicks: "))
    impression = int(input("Enter Total impression: "))
    revenue = float(input("Enter Total revenue: "))

    metrics = DailyMetrics(spend, impression, clicks, revenue)
    mode = input("Select mode 'auto' or 'manual': ")

    if mode.lower() == "manual":
        scale_ctr = float(input("Scale when CTR >= : "))
        scale_cpc = float(input("Scale when CPC <= : "))
        scale_roas = float(input("Scale when ROAS >= : "))
        stop_ctr = float(input("Stop when CTR <= : "))
        stop_cpc = float(input("Stop when CPC >= : "))
        stop_roas = float(input("Stop when ROAS <= : "))
        engine = EngineRuleUserDefined(metrics.ctr, metrics.cpc, metrics.roas, scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas)
    else:
        engine = EngineRuleAutomated(metrics.ctr, metrics.cpc, metrics.roas)

    print(engine.decision())

except ValueError:
    print("Please Enter Valid Input.....")