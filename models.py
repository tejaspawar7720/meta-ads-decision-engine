class DailyMetrics:
    """This class function is use to call daily metrics 
as user enters there spend impression clicks and revenue
then it convert into the ctr cpc and roas automatically"""
    def __init__(self, spend : float, impression : int , clicks : int, revenue : float):
        if clicks == 0:
            raise ValueError("clicks can not be Zero / 0 ")
        if impression == 0:
            raise ValueError("Impressions Can not be Zero / 0")
        if spend == 0:
            raise ValueError("Spend Can not be zero / 0")
        self.ctr = (clicks / impression) * 100
        self.cpc = spend / clicks
        self.roas = revenue / spend