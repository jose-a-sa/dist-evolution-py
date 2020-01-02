import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


class DiscreteEvolution:
    def __init__(self, num_bots, initial_q, num_iter=100000):
        self.__cnt = 0
        self._states = self.__initialize_array(num_bots, initial_q, num_iter)
        self.__init_sns()

    def __initialize_array(self, num_bots, initial_q, num_iter):
        q_array = np.array([initial_q] * num_bots)
        result = np.array([q_array] * (num_iter + 1))
        return result

    def _num_bots(self):
        return self._states[0].shape[0]

    def _num_iterations(self):
        return list(self._states.shape)[0]

    def _initial_q(self):
        return self._states[0][0]

    def get_states(self):
        return self._states

    def get_state(self, i):
        if(i < self._num_iterations()):
            result = self._states[i]
        else:
            result = np.array([])
        return result

    def _unit_transation(self, state):
        i = rnd.randint(self._num_bots())
        while(state[i] == 0):
            i = rnd.randint(self._num_bots())

        j = rnd.randint(self._num_bots())
        while(state[j] == 0 or j == i):
            j = rnd.randint(self._num_bots())

        coinToss = rnd.rand() < 1/2
        state[[i, j]] += [+1, -1] if(coinToss) else [-1, +1]

        return state

    def evolve(self, steps=1):
        j = 0
        while(j < steps and self.__cnt < self._num_iterations()):
            self._states[self.__cnt+1] = self._unit_transation(self._states[self.__cnt].copy())
            self.__cnt += 1
            j += 1
        return self.get_state(self.__cnt)

    def save_states_csv(self, fname="0.csv"):
        np.savetxt(fname, self.get_states(),
                   fmt=','.join(['%i']*self._num_bots()))

    def __init_sns(self):
        sns.axes_style("darkgrid")
        sns.set(context="paper", style="darkgrid", font_scale=1.2)

    def save_distplot(self, i=-1, fmt="{}.png"):
        c = sns.color_palette(None, 7)
        fig = plt.figure(figsize=(6, 4))
        plt.axes(xlim=(0, 120))
        sns.distplot(self.get_state(i), bins=20, kde=False, fit=stats.pareto,
                     fit_kws={"label": "Pareto", "color": c[0]})
        sns.distplot(self.get_state(i), kde=False, hist=False, fit=stats.norm,
                     fit_kws={"label": "Norm", "color": c[1]})
        lg = plt.legend(fancybox=True, frameon=True)
        lg.get_frame().set_facecolor('white')
        fig.savefig(fmt.format(i))
        plt.close(fig)
