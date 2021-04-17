import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def generate(matt = [1,1,1,1], connor = [2,2,2,2], jacob = [3,3,3,3], eric = [4,4,4,4]):
    plt.plot(matt, 'r', connor, 'b', jacob, 'g', eric, 'y' )
    matt_patch = mpatches.Patch(color = 'red', label = 'Matt')
    connor_patch = mpatches.Patch(color='blue', label='Connor')
    jacob_patch = mpatches.Patch(color='green', label='Jacob')
    eric_patch = mpatches.Patch(color='yellow', label='Eric')
    plt.xlabel('Hours')
    plt.ylabel('Cups of Coffee')
    plt.legend(loc='upper left', handles = [matt_patch,connor_patch,jacob_patch,eric_patch])
    plt.savefig('..\static\coffee.png')
    pass

generate()