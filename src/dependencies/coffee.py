import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from db import db


def generate(data):
    plotData = [list(range(30)), list(range(30)), list(range(30)), list(range(30))]
    for i in range(4):
        for j in range(30):
            plotData[i][j] = 0

    #cups for each hour
    for d in data:
        if (d[0] == 'matt'):
            plotData[0][d[1]] += d[2]
        elif (d[0] == 'connor'):
            plotData[1][d[1]] += d[2]
        elif (d[0] == 'jacob'):
            plotData[2][d[1]] += d[2]
        elif (d[0] == 'eric'):
            plotData[3][d[1]] += d[2]

    #total cups over time
    for l in plotData:
        for i in range(29, 0, -1):
            l[i] += sum(l[0:i])

    plt.plot(plotData[0], 'r', plotData[1], 'b', plotData[2], 'g', plotData[3], 'y')

    matt_patch = mpatches.Patch(color='red', label='Matt')
    connor_patch = mpatches.Patch(color='blue', label='Connor')
    jacob_patch = mpatches.Patch(color='green', label='Jacob')
    eric_patch = mpatches.Patch(color='yellow', label='Eric')
    plt.xlabel('Hours')
    plt.ylabel('Total Cups of Coffee')
    plt.legend(loc='upper left', handles=[matt_patch, connor_patch, jacob_patch, eric_patch])
    plt.savefig('..\static\coffee.png')


d = db(host = '192.168.1.100')
generate(d.getCoffeeData())
