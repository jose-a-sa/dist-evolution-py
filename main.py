import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.stats as stats
import seaborn as sns


def main():
    nBots = 500
    initialMoney = 10
    nIterations = 100000

    states = initializeArray(nBots, initialMoney, nIterations)

    i = 0
    while(i < nIterations):
        states[i+1] = unitTransation(states[i].copy())
        i += 1

    initSeaborn()
    
    for i in range(1, nIterations+1, 50):
        saveState(states[i], i//50)


def initializeArray(nBots, initialMoney, nIterations=0):
    moneyArray = np.array([initialMoney] * nBots)
    result = np.array([moneyArray] * (nIterations + 1))
    return result


def unitTransation(state):
    nBots = state.shape[0]

    i = np.random.randint(nBots)
    while(state[i] == 0):
        i = np.random.randint(nBots)

    j = np.random.randint(nBots)
    while(state[j] == 0 or j == i):
        j = np.random.randint(nBots)

    coinToss = np.random.rand() < 1/2
    state[[i, j]] += [+1, -1] if(coinToss) else [-1, +1]

    return state


def initSeaborn():
    sns.axes_style("darkgrid")
    sns.set(context="paper", style="darkgrid", font_scale=1.2)


def saveState(state, name=0):
    colorPallette = sns.color_palette(None, 7)
    fig = plt.figure(figsize=(6, 4))
    plt.axes(xlim=(0, 120), ylim=(0, 0.15))
    # plt.grid(color="w", alpha=0.3, linestyle="--")
    sns.distplot(state, bins=20, kde=False, fit=stats.pareto,
                 fit_kws={"label": "Pareto", "color": colorPallette[0]})
    sns.distplot(state, kde=False, hist=False, fit=stats.norm,
                 fit_kws={"label": "Norm", "color": colorPallette[1]})
    lg = plt.legend(fancybox=True, frameon=True)
    lg.get_frame().set_facecolor('white')
    fig.savefig("out1/{}.png".format(name))
    plt.close(fig)


if __name__ == "__main__":
    main()
