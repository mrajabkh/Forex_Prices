import matplotlib.pyplot as pit
import pandas as pd
import numpy as np
import csv

'''
with open('Year 3 and Year 4.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
'''

df = pd.read_csv("Year 3 and Year 4.csv")
df = df[["Date","Close"]]


