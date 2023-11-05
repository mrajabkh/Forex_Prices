import pandas as pd
import numpy as np
import random



def year(count,limit,yr):
    c=0
    df = pd.read_csv("GBPUSD.csv")
    df = df[["Date", "Close"]]
    ddf = df[count:count + 1]
    original = count
    first = True
    while count < limit: #120 per week, 360 for 3 weeks, 1 year is 6240 +1
        for i in range(0,6): #write to file instead
            if first == True:
                count += 24
                ddf = pd.concat([ddf, df[count:count + 1]])
                count += 24
                ddf = pd.concat([ddf, df[count:count + 1]])
                count += 24
                ddf = pd.concat([ddf, df[count:count + 1]])
                count += 21
                ddf = pd.concat([ddf, df[count:count + 1]])
                count += 3
                first = False
                break
            elif i < 4:
                count += 24
            elif i == 4:
                count += 21
            elif i == 5:
                count += 3
            ddf = pd.concat([ddf, df[count:count + 1]])
    ddf.to_csv('data.csv', sep=',' , index=False)
    print(ddf.to_string())


    
    

year(23, 6246,0)
#year(6270, 12471,1)
#year(12495, 18735,2)

def old():
    df = pd.read_csv("ThreeWeeks.csv")
    df = df[["Date", "Close"]]
    count = 23
    ddf = df[count:count + 1]
    while count < 361: #120 per week, 360 for 3 weeks
        for i in range(0,5): #write to file instead
            if i < 3:
                count += 24
            elif i == 3:
                count += 21
            elif i == 4:
                count += 3
            ddf = pd.concat([ddf, df[count:count + 1]])
    print(ddf.to_string())
    ddf.to_csv("data.csv", sep=",", encoding="utf-8")
def days(filename):
    df = pd.read_csv("SingleDay.csv")
    df = df[["Date", "Close"]]
    df = df[count:]
   # file.append(df.to_string())
    count += a
    #write to new file
def day7():
    df = pd.read_csv("SingleDay.csv")
    df = df[["Date", "Close"]]
    df = df[count:]
    count += b
    #write to new file   
#print(df.to_string())