def get_manual_thresholds() -> tuple:
    """This function is use to get input from user
    to define there manually and set rules accordning to user for scale hold and stop """
    scale_ctr = float(input("Scale when CTR >= : "))
    scale_cpc = float(input("Scale when CPC <= : "))
    scale_roas = float(input("Scale when ROAS >= : "))
    stop_ctr = float(input("Stop when CTR <= : "))
    stop_cpc = float(input("Stop when CPC >= : "))
    stop_roas = float(input("Stop when ROAS <= : "))
    return scale_ctr, scale_cpc, scale_roas, stop_ctr, stop_cpc, stop_roas

