import matplotlib.pyplot as plt
import numpy as np


def generate(matt = [1,1,1,1], connor = [2,2,2,2], jacob = [3,3,3,3], eric = [4,4,4,4]):
    plt.plot(matt, 'r', connor, 'b', jacob, 'g', eric, 'y' )
    plt.savefig('..\static\coffee.png')
    pass

generate()