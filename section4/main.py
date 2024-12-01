import pandas as pd
import matplotlib as plt
import yfinance as yf

aapl = yf.Ticker('AAPL')

days = 5
hist = aapl.history(period=f'{days}d')
