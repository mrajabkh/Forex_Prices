import csv
import matplotlib.pyplot as plt
import numpy as np


file = open("Year 3 and Year 4.csv","r")
data = list(csv.reader(file,delimiter=","))
file.close()

Yr3Date = []
Yr3Close = []
Yr4Date = []
Yr4Close = []


for i in range (0,len(data[0])-1):
    #Yr3Date.append(data[1][i])
    #Yr3Close.append(data[2][i])

'''
for j in range (0,len(data[2])-1):
    Yr4Date.append(data[3][j])
    Yr4Close.append(data[4][j])


xpoints = np.array(Yr3Date)
ypoints = np.array(Yr3Close)

plt.plot(xpoints,ypoints)

plt.xlabel("Date")
plt.ylabel("Close")
plt.title("Bullshit Comparsion between Year 3 and year 4")
'''
plt.show()




