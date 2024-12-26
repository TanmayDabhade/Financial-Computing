import yfinance as yf

class Financial_Analysis():
    def __init__(self, symbol = "NFLX"):
        self.symbol = symbol

    def fetch_financial_data(self):
        symbol = self.symbol.capitalize()
        print("Fetching data...")
        ticker = yf.Ticker(symbol)

        # Get historical market data
        hist_1_day = ticker.history(period="1d")
        hist_5_day = ticker.history(period="5d")
        hist_1_month = ticker.history(period="1mo")
        hist_3_month = ticker.history(period="3mo")
        hist_6_month = ticker.history(period="6mo")
        hist_1_year = ticker.history(period="1y")
        hist_2_year = ticker.history(period="2y")
        hist_5_year = ticker.history(period="5y")
        hist_10_year = ticker.history(period="10y")
        hist_ytd = ticker.history(period="ytd")

        data_dict = {
            'hist_1_day': hist_1_day,
            'hist_5_day': hist_5_day,
            'hist_1_month': hist_1_month,
            'hist_3_month': hist_3_month,
            'hist_6_month': hist_6_month,
            'hist_1_year': hist_1_year,
            'hist_2_year': hist_2_year,
            'hist_5_year': hist_5_year,
            'hist_10_year': hist_10_year,
            'hist_ytd': hist_ytd
        }

        for name, data in data_dict.items():
            data.to_csv(f"../financial_computing/csv_data/{name}.csv")

        print("Completed fetching data and updated to csv files.")

    
