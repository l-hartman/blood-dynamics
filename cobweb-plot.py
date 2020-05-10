import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style="ticks")


def create_plots(mapping, r, seed, iterations, save=False):
    fig, ax = plt.subplots()
    fx_x = np.linspace(0, 1, 1000)
    c_xs, c_ys = cobweb(mapping, iterations, seed, r)

    ax.plot(fx_x, fx_x, c="#cfeed1")
    ax.plot(fx_x, mapping(fx_x, r), c="#ff2768")
    ax.plot(c_xs, c_ys, c="black", alpha=0.7)

    ax.set_aspect("equal")
    ax.grid(True, which="both")
    seaborn.despine(ax=ax, offset=0)
    plt.show()

def cobweb(mapping, iterations, seed, r):
    """generate cobweb diagram points"""
    xs = np.zeros((iterations+1, 2))
    ys = np.zeros((iterations+1, 2))

    # start at (x=seed, y=0)
    xs[0] = seed 
    ys[0] = 0

    i = 1
    while i < iterations:
        old_x = xs[i-1]

        # get next point on map
        xs[i] = old_x
        ys[i] = mapping(old_x, r)

        # get next y=x point
        xs[i+1] = ys[i]
        ys[i+1] = ys[i]
        i += 2

    return xs, ys 



def function(x, r):
    """map"""
    return r * x * (1 - x)

def function1(x, r):
    return np.cos(x)

def function2(x, r):
    return x * x * x 


if __name__=="__main__":
    create_plots(function, 2.6, 0.1, 20)
    create_plots(function1, 2.6, .5, 20)
    create_plots(function1, 0.6, 1, 20)
    create_plots(function2, 2.0, .3, 20)
    create_plots(function2, 2.6, .9, 20)

