import math
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style="ticks")


class Model(object):
    """
        x_n+1 - x_n = p(x_n) - d(x_n)o

        where:
            x_n is the blood cell count at time n;
            p is a function that represents the number of cells produced in one time unit;
            d is a function that measures the number of cells destroyed in one time unit;
    """

    def __init__(self, a, b, r, s):
        # destruction coefficient, # between 0 and 1
        self.a = a
        self.b = b
        self.r = r 
        self.s = s 
        # control parameter, element of R4
        self.a_bar = (self.a, self.b, self.r, self.s)

    def p(self, x_n):
        """Lasota (1977) production function"""
        return self.b * x_n ** self.r * math.e ** (-self.s * x_n)

    def d(self, x_n):
        """for each timestep a constant fraction of cells are destroyed"""
        return self.a * x_n

    def f(self, x):
        return (1 - self.a) * x + self.p(x)

def plot(m, x_range, y_range, filename=None):
    func = m.f
    fig, ax = plt.subplots()
    xs = np.linspace(x_range[0], x_range[1], 1000)

    ax.plot(xs, xs, c="#764439")
    ax.plot(xs, func(xs), c="#ff2768") 

    ax.set_aspect("equal")
    ax.grid(True, which="both")
    seaborn.despine(ax=ax, offset=0)
    plt.show()


def main():
    # model analysis
    m = Model(0.2, 4, 6, 2)
    # create plot on the region [0,10] x [0,10]
    plot(m, (0, 10), (0, 10), filename="model_analysis1.png")
    # create plot on the region [0,1] x [0,1]
    plot(m, (0, 1), (0, 1), filename="model_analysis2.png")

if __name__ == "__main__":
    main()
