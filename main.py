import linecache as lc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

from DiscreteEvolution import DiscreteEvolution


def main():
    n_bots = 500
    initial_money = 10
    n_iter = 100000
    
    plt.rcParams["patch.force_edgecolor"] = True

    for i in range(n_iter//20):
        print(i)
        to_plot(i*20, "img/{}.png".format(i))


def load_lines(line_no, fmt="out/{}.csv"):
    line = ""
    for i in range(100):
        line += lc.getline(fmt.format(i), line_no+1).rstrip() + ","
        lc.clearcache()
    return np.array([int(x) for x in line.rstrip(',').split(',')])


def to_plot(i, fmt="img/{}.png"):
    data = load_lines(i)
    fig = plt.figure(figsize=(8, 6))
    plt.axes(xlim=(0, 60))
    sns.distplot(data, bins=16, kde=False, hist_kws={
                 "edgecolor": "k", "linewidth": 1})
    # lg = plt.legend(fancybox=True, frameon=True)
    # lg.get_frame().set_facecolor('white')
    fig.savefig(fmt.format(i), dpi=600)
    plt.close(fig)


if __name__ == "__main__":
    main()
