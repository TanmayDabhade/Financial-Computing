import pandas as pd
from fetch_data import FetchData

data_dict = {
    '1d': 'hist_1_day',
    '5d': 'hist_5_day',
    '1mo': 'hist_1_month',
    '3mo': 'hist_3_month',
    '6mo': 'hist_6_month',
    '1y': 'hist_1_year',
    '2y': 'hist_2_year',
    '5y': 'hist_5_year',
    '10y': 'hist_10_year',
    'ytd': 'hist_ytd'
}

def fetch_data():
    ticker_symbol = input("Enter stock symbol(ex. NFLX, AAPL, etc.): ")
    FetchData(ticker_symbol).fetch_financial_data()

def load_data(time_frame = 'ytd', data= data_dict):
    data_frame = pd.read_csv(f'../financial_computing/csv_data/{data[time_frame]}.csv')
    return data_frame

def Volume_Weighted_Average_Price(data):
    '''Only to be used when data is for 5 day time frame'''
    Volume_Weighted_Average_Price_Value = 0
    for i in range(len(data)):
        price_T = (data.High[i] + data.Low[i] + data.Close[i]) / 3
        volume_T = data.Volume[i]
        Volume_Weighted_Average_Price_Value += (price_T * volume_T) / sum(data.Volume)
    print(f'VWAP for 5days in symbol is {Volume_Weighted_Average_Price_Value}')
    return Volume_Weighted_Average_Price_Value

def Simple_Moving_Average(data):
    Simple_Moving_Average_Value = sum(data.Close) / len(data)
    print(f'Simple Moving Average for given symbol is {Simple_Moving_Average_Value}')
    return Simple_Moving_Average_Value



def main():
    fetch_data()
    financial_data = load_data('5d', data_dict)
    Volume_Weighted_Average_Price(financial_data)
    Simple_Moving_Average(financial_data)



if __name__ == "__main__":
    main()