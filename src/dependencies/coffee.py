import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def generate(data):


    #plt.plot(data[0], 'r', data[1], 'b', data[2], 'g', data[3], 'y' )
    matt_patch = mpatches.Patch(color = 'red', label = 'Matt')
    connor_patch = mpatches.Patch(color='blue', label='Connor')
    jacob_patch = mpatches.Patch(color='green', label='Jacob')
    eric_patch = mpatches.Patch(color='yellow', label='Eric')
    plt.xlabel('Hours')
    plt.ylabel('Cups of Coffee')
    plt.legend(loc='upper left', handles = [matt_patch,connor_patch,jacob_patch,eric_patch])
    plt.savefig('..\static\coffee.png')

generate()