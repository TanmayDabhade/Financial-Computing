import pandas as pd
from fetch_data import FetchData

class FinancialAnalysis():
    def __init__(self, data):
        self.data = data

    def Volume_Weighted_Average_Price(self):
        '''Only to be used when data is for 5 day time frame'''
        Volume_Weighted_Average_Price_Value = 0
        for i in range(len(self.data)):
            price_T = (self.data.high[i] + self.data.low[i] + self.data.close[i]) / 3
            volume_T = self.data.volume[i]
            Volume_Weighted_Average_Price_Value += (price_T * volume_T) / sum(self.data.Volume)
        print(f'VWAP for 5days in symbol is {Volume_Weighted_Average_Price_Value}')
        return Volume_Weighted_Average_Price_Value

    # def Standard_Deviation_Stock(data):
    #     standard_deviation_close = data['Close'].std()
    #     standard_deviation_high = data['High'].std()
    #     standard_deviation_low = data['Low'].std()
    #     print(f'Standard Deviation of high price for given symbol is {standard_deviation_high}')
    #     print(f'Standard Deviation of low price for given symbol is {standard_deviation_low}')
    #     print(f'Standard Deviation of closing price for given symbol is {standard_deviation_close}')
    #     return standard_deviation_close, standard_deviation_high, standard_deviation_low

    # def Simple_Moving_Average(data):
    #     Simple_Moving_Average_Value = sum(data.Close) / len(data)
    #     print(f'Simple Moving Average for given symbol is {Simple_Moving_Average_Value}')
    #     return Simple_Moving_Average_Value

    # def Exponential_Moving_Average(data):
    #     pass


