class TrendAnalyzer:
    """ This class is use to enter or analyze the last 3 days(Max) data 
    and give decision base on that 3/d data"""
    def __init__(self, days_data : list):
        self.days = days_data
    
    def decision(self) -> str:
        if self.days[0]["ctr"] < self.days[1]["ctr"] < self.days[2]["ctr"] and self.days[0]["cpc"] > self.days[1]["cpc"] > self.days[2]["cpc"] and self.days[0]["roas"] < self.days[1]["roas"] < self.days[2]["roas"]:
            return "Scale..."
        else:
            return "Hold..."