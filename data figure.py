import datetime as dt
import pandas as pd
from datetime import date
import mplfinance as mpl
from matplotlib import pyplot as plt
from datetime import date
import pandas_datareader.data as web
from matplotlib import style
style.use('ggplot')
start = date.today()
end= dt.datetime(2016,1,1)
df = web.DataReader('NKE','yahoo',end,start)
mpl.plot(df,type='line',title='Tesla Stock Prices in 2016/21',tight_layout=True,style='yahoo')