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

for i in range (1,len(data[1])):
    Yr3Date.append(data[i][0])
    Yr3Close.append(data[i][1])

for j in range (1,len(data[3])):
    Yr4Date.append(data[i][2])
    Yr4Close.append(data[i][3])


xpoints = np.array(Yr3Date)
ypoints = np.array(Yr3Close)
xpoints1 = np.array(Yr4Date)
ypoints1 = np.array(Yr4Close)
#plt.plot(xpoints,ypoints)
plt.plot(xpoints1,ypoints1)

plt.xlabel("Date")
plt.ylabel("Close")
plt.title("Bullshit Comparsion between Year 3 and year 4")

plt.show()






