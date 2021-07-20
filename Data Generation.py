import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
file = open('Stock Prices.csv','a')
csv_writer= csv.writer(file)
data = pd.read_csv('Stock Prices.csv')
stock_codes=['NKE']
cols=[]
def stockcodeprice(stock_codes):
    for stock_code in stock_codes:
        link = 'https://finance.yahoo.com/quote/'+stock_code+'?p='+stock_code
        page = requests.get(link).text
        soup = BeautifulSoup(page,'lxml')
        name = soup.find('h1',class_='D(ib) Fz(18px)').text
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        price = soup.find('div',class_='D(ib) Mend(20px)').span.text
        cols.append([stock_code,name,current_time,price,date.today()])
    for col in cols:
        csv_writer.writerow(col)
        print('Stock code : ',col[0],'\nStcok Full name : ',col[1],'\nTime Checked: ',col[2],'\nStock Price : ',col[3],'\nFull date : ',col[4],'\n')


while True:
    time.sleep(10)
    stockcodeprice(stock_codes)