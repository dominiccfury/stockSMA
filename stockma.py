import os
import sys
import keyboard
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

def smacalc():
    yf.pdr_override()

    stock=input("Enter a ticker: ")
    startyear= int(input("Enter the start year: "))
    startmonth= int(input("Enter the start month (1-12): "))
    startday= int (input("Enter the start day (i. e: 1,2,3): "))
    ma= int (input("Enter a timeframe in days for the moving average \n(i. e: 50 for a 50 day moving average: "))


    print(stock)
    start=dt.datetime(startyear,startmonth,startday)
    now=dt.datetime.now()


    df=pdr.get_data_yahoo(stock,start,now)





    smaString="Sma_"+str(ma)+" day"

    df[smaString]=df.iloc[:,4].rolling(window=ma).mean()



    df=df.iloc[ma:]

    numH=0
    numC=0

    for i in df.index:
        if(df["Adj Close"][i]>df[smaString][i]):
            print( i, "The Close is Higher")
            numH+=1
        else:
            print( i, "The Close is lower")
            numC+=1

    print("\nClosed higher than", "Sma_"+str(ma)+" day:",str(numH), "times")
    print("Closed lower than", " Sma_"+str(ma)+" day:",str(numC), "times \n\n")

    print(stock)
    print(df)
    

while True:
    smacalc()
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        smacalc()
    else:
        print("Goodbye")
        break