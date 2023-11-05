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
    df = pd.read_csv("SingleDay.csv")
    df = df[["Date", "Close"]]
    count = 23
    ddf = df[count:count + 1]
    print(ddf.to_string())
    while count < 361:
        for i in range(0,6):
            if i < 4:
                count += 24
            elif i == 4:
                count += 21
            elif i == 5:
                count += 3
            ddf = df[count:count + 1]
            print(ddf.to_string())

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





print(df.to_string())