import yfinance as yf

tickers = ['AAPL', 'COG', 'GE', 'MSFT', 'NFLX', 'TSLA', '^GSPC']
stock_data = yf.download(tickers, start="2016-08-1", end="2022-10-26")

rf = 0.01307
daily_returns = stock_data['Adj Close'].pct_change().dropna()
rm = daily_returns['^GSPC'].mean() * 252

cov = daily_returns.cov()
var = daily_returns['^GSPC'].var()
beta_aapl = cov.loc['AAPL', '^GSPC']/ var

r_aapl = rf + (beta_aapl * (rm-rf))
print("Expected rate of return on AAPL is: " + str(r_aapl))

beta = cov.loc['^GSPC']/ var
r_stocklist = rf + (beta * (rm-rf))
print(r_stocklist)
    
    