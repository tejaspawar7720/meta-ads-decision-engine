
class EngineRuleAutomated:
        def __init__(self, ctr : float, cpc : float, raos : float ):
            self.ctr = ctr
            self.cpc = cpc
            self.raos = raos

        def dicision(self):
            if self.ctr >= 1 and self.cpc <= 10 and self.raos >= 3:
                return "Scale..."
            elif self.ctr <= 0.70 and self.cpc >= 20 and self.raos <= 2:
                return "Stop..."
            else:
                return "Hold..."
#engine = EngineRuleAutomated(ctr=0.70, cpc=20, raos=2)
#print(engine.dicision())

class EngineRuleUserDefined:
    def __init__(self, ctrU, cpcU, raosU, scale_ctr, scale_cpc, scale_raos, stop_ctr, stop_cpc, stop_raos):
         self.ctrU = ctrU
         self.cpcU = cpcU
         self.raosU = raosU
         self.scale_ctr = scale_ctr
         self.scale_cpc = scale_cpc
         self.scale_raos = scale_raos
         self.stop_ctr = stop_ctr
         self.stop_cpc = stop_cpc
         self.stop_raos = stop_raos
    def disicion(self):
        if self.ctrU >= self.scale_ctr and self.cpcU <= self.scale_cpc and self.raosU >= self.scale_raos:
            return "Scale..."
        elif self.ctrU <= self.stop_ctr and self.cpcU >= self.stop_cpc and self.raosU <= self.stop_raos:
             return "Stop..."
        else:
             return "Hold..."
try: 
    scale_ctr = float(input("Enter Ctr Rule when to scale: "))
    scale_cpc = float(input("Enter CPC Rule when to scale: "))
    scale_raos = float(input("Enter Raos Rule when to scale: "))
    stop_ctr = float(input("Enter Ctr Rule when to stop: "))
    stop_cpc = float(input("Enter CPC Rule when to stop: "))
    stop_raos = float(input("Enter Raos Rule when to stop: "))
    ctrU = float(input("Enter Your Current CTR: "))
    cpcU = float(input("Enter You current CPC : "))
    raosU = float(input("Enter Your Current Raos: "))

    userEngine = EngineRuleUserDefined(ctrU, cpcU, raosU, scale_ctr, scale_cpc, scale_raos, stop_ctr, stop_cpc, stop_raos)
    print(userEngine.disicion())

except ValueError:
     print("Please Enter Valid Input.....")

