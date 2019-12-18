import pandas as pd
import pandas_datareader.data as web

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
# gs.tail()

ma5 = gs['Adj Close'].rolling(window=5).mean()

type(ma5)
# ma5.tail(10)

new_gs = gs[gs['Volume'] != 0]
# new_gs.tail()

ma5 = new_gs['Adj Close'].rolling(window=5).mean()
# ma5.tail(10)

new_gs.insert(len(new_gs.columns), "MA5", ma5)
# new_gs.tail(5)

ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

# new_gs.tail()