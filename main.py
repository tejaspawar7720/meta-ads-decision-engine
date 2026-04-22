from models import DailyMetrics
from engines import EngineRuleAutomated, EngineRuleUserDefined
from analyzers import TrendAnalyzer
from utils import get_manual_thresholds

try:
    #This is use to handle exceptiona while user 
    # entering invalid values like string and inside that there is 
    # a loop that runs till max 3 days and get input and store's in the list
    # then there is a selector that ask user to select daily or last 3 day data

    daymode = input("Enter a data you want to enter, Enter 1 for daily and 3 for last 3 days: ")  
    if daymode.lower() == "3":
        #this start loop till day 3 when user selected day 3   
        days_data = []
        for i in range(3):
            print(f"\nDay {i+1} data:")
            spend = float(input("Spend: "))
            clicks = int(input("Clicks: "))
            impression = int(input("Impressions: "))
            revenue = float(input("Revenue: "))
                
            metrics = DailyMetrics(spend, impression, clicks, revenue)
            days_data.append({
                "ctr":metrics.ctr,
                "cpc": metrics.cpc,
                "roas": metrics.roas,
            })
        mode = input("Select mode 'auto' or 'manual': ")

        if mode.lower() == "manual":
            scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas = get_manual_thresholds()
            engine = EngineRuleUserDefined(metrics.ctr, metrics.cpc, metrics.roas, scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas)
            print(engine.decision())
            analyzer = TrendAnalyzer(days_data)
            print(analyzer.decision())
        else:
            engine = EngineRuleAutomated(metrics.ctr, metrics.cpc, metrics.roas)
            print(engine.decision())
            analyzer = TrendAnalyzer(days_data)
            print(analyzer.decision()) 
    else:
        #this is the else case if user selected one day data to analyze
        spend = float(input("Enter Total spend: $"))
        clicks = int(input("Enter Total Clicks: "))
        impression = int(input("Enter Total impression: "))
        revenue = float(input("Enter Total revenue: "))

        metrics = DailyMetrics(spend, impression, clicks, revenue)
        mode = input("Select mode 'auto' or 'manual': ")
        #one more mode selector to ask user first if he want automated rules or 
        # he want to decide what rules should be
        if mode.lower() == "manual":
            #manual mode when user selects manual
            scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas = get_manual_thresholds()
            engine = EngineRuleUserDefined(metrics.ctr, metrics.cpc, metrics.roas, scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas)
            print(engine.decision())
                
        else:
            # when user select auto mode it call the automated engine rules 
            # and send data to the automtedenginerule class
            engine = EngineRuleAutomated(metrics.ctr, metrics.cpc, metrics.roas)
            print(engine.decision())


except ValueError:
        print("Please Enter Valid Input.....")