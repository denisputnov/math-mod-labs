import warnings

import numpy as np
from matplotlib import pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)


def drawGraphic(a, b, func):
    x = np.linspace(a, b, 10000)
    plt.plot(x, func(x))
    plt.show()