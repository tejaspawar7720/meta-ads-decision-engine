class EngineRuleAutomated:
    """this class is use to give user automatic decision base 
    on there metrics and rules are already set by the developer"""
    def __init__(self, ctr : float, cpc : float, roas : float):
        self.ctr = ctr
        self.cpc = cpc
        self.roas = roas

    def decision(self) -> str:
        if self.ctr >= 1 and self.cpc <= 10 and self.roas >= 3:
            return "Scale..."
        elif self.ctr <= 0.70 and self.cpc >= 20 and self.roas <= 2:
            return "Stop..."
        else:
            return "Hold..."
        
        
class EngineRuleUserDefined:
    """This class is use to define rules that is being 
entered by the user to set rules as the user want and give them decision"""
    def __init__(self, ctr : float, cpc:float, roas:float, scale_ctr:float, scale_cpc:float, scale_roas:float, stop_ctr:float, stop_cpc:float, stop_roas:float):
        self.ctr = ctr
        self.cpc = cpc
        self.roas = roas
        self.scale_ctr = scale_ctr
        self.scale_cpc = scale_cpc
        self.scale_roas = scale_roas
        self.stop_ctr = stop_ctr
        self.stop_cpc = stop_cpc
        self.stop_roas = stop_roas

    def decision(self) -> str:
        if self.ctr >= self.scale_ctr and self.cpc <= self.scale_cpc and self.roas >= self.scale_roas:
            return "Scale..."
        elif self.ctr <= self.stop_ctr and self.cpc >= self.stop_cpc and self.roas <= self.stop_roas:
            return "Stop..."
        else:
            return "Hold..."