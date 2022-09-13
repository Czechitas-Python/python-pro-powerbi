import yfinance as yf
import pandas


msft = yf.Ticker("MSFT")
msft_df = msft.history(period="1y")
msft_df.describe()
aapl = yf.Ticker("AAPL")
aapl_df = aapl.history(period="1y")
msft_close = msft_df["Close"]
aapl_close = aapl_df["Close"]

stock_data_df = pandas.merge(msft_close, aapl_close, on=["Date"], suffixes=["MSFT", "AAPL"])
stock_data_df = stock_data_df.rename(columns={"CloseMSFT": "MSFT", "CloseAAPL": "AAPL"})

tsn = yf.Ticker("TSN")
tsn_df = tsn.history(period="1y")
tsn_df = tsn_df.rename(columns={"Close": "TSN"})
tsn_close = tsn_df["TSN"]
stock_data_three_df = pandas.merge(stock_data_df, tsn_close, on=["Date"])

pm = yf.Ticker("PM")
pm_df = pm.history(period="1y")
pm_df = pm_df.rename(columns={"Close": "PM"})
pm_close = pm_df["PM"]
stock_data_three_df = pandas.merge(stock_data_three_df, pm_close, on=["Date"])

meta = yf.Ticker("META")
meta_df = meta.history(period="1y")
meta_df = meta_df.rename(columns={"Close": "META"})
meta_close = meta_df["META"]
stock_data_three_df = pandas.merge(stock_data_three_df, meta_close, on=["Date"])

print(stock_data_three_df.head())
stock_data_three_df["MSFT_change"] = stock_data_three_df["MSFT"].pct_change()
stock_data_three_df["AAPL_change"] = stock_data_three_df["AAPL"].pct_change()
stock_data_three_df["TSN_change"] = stock_data_three_df["TSN"].pct_change()
stock_data_three_df["PM_change"] = stock_data_three_df["PM"].pct_change()
stock_data_three_df["META_change"] = stock_data_three_df["META"].pct_change()
stock_data_three_df.to_csv("stock_data.csv")
