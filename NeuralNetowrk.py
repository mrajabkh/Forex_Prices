import pandas as pd
import numpy as np
import random

"""end = False

file_object = open("data.txt","w")
file_object.close();

while end == False:
    #days(data.txt)
    end = True

df = pd.read_csv("SingleDay.csv")
df = df[["Date", "Close"]]
df = df[23:]"""


def week():
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
    ddf.to_csv("data.csv", sep="\t", encoding="utf-8")

week()



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