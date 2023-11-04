import pandas as pd
import numpy as np
import random

global count
count = 23
a = 23
b = 3
end = False

file_object = open("data.txt","w")
file_object.close();

while end == False:
    #days(data.txt)
    end = True

df = pd.read_csv("SingleDay.csv")
df = df[["Date", "Close"]]
df = df[23:]

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