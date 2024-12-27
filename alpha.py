from alpha_vantage.timeseries import TimeSeries
from finance_analysis import FinancialAnalysis

def fetch_data():
    # API Key for Alpha Vantage
    api_key = 'YOUR_API_KEY'

    # Create a TimeSeries instance
    ts = TimeSeries(key=api_key, output_format='csv')

    # Fetch intraday data (1-minute interval)
    data, meta_data = ts.get_intraday(symbol='AAPL', interval='1min', outputsize='full')

    # Display the data


    data.to_csv(f"../financial_computing/csv_data/alpha.csv")
                        
    return data



def main():
    data = fetch_data()
    print(data)

    # FinancialAnalysis(data).Volume_Weighted_Average_Price()


if __name__ == "__main__":
    main()