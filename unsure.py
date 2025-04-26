'''
r(min, mode, max): PERT distribution (recommended), takes the mininum, most likely, and maximum value
n(a, b): normal distribution, 90% confidence values are between `a` and `b`
u(a, b): uniform distribution between `a` and `b`

hist(np.array): convert from an array of random samples. size should match hist._samples to interact with other distrubutions
distributions inherit np.ndarray, so you can use any array operations on these objects (np.exp, np.std, np.quantile, plt.hist, sns.kdeplot, etc)

example usage:
>>> r(1400,1500,1700) * r(0.55,0.60,0.65) - r(600,620,700) - r(100,120,200) - 30 - 20

35.72~165.8  # (this is the 90% confidence window)

100.0% |  above | ▒▒
 99.5% |  223.5 | ▒▒
 98.9% |  210.9 | ▒▒▒▒
 98.0% |  198.2 | ▒▒▒▒▒▒
 96.4% |  185.6 | ▒▒▒▒▒▒▒▒▒▒
 93.9% |  173   | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 90.3% |  160.4 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 85.4% |  147.7 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 79.3% |  135.1 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 71.6% |  122.5 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 62.9% |  109.8 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 53.5% |  97.22 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  (median = 99.02798633335368)
 43.7% |  84.59 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 34.1% |  71.96 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 25.4% |  59.33 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 17.9% |  46.71 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 11.9% |  34.08 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  7.3% |  21.45 | ▒▒▒▒▒▒▒▒▒▒▒▒
  4.2% |  8.823 | ▒▒▒▒▒▒▒▒
  2.2% | -3.805 | ▒▒▒▒
  1.1% | -16.43 | ▒▒
  0.5% |  below | ▒▒

>>> g = r(0,50,100)
>>> (g>20) & (g<40)
True  |  26.0% | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
False |  74.0% | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

for more information see Unsure Calculator https://filiph.github.io/unsure/
''';
import numpy as np
class hist(np.ndarray):
    '''Base class for distributions. plots a histogram'''
    _max_width = 40  # max bar width in characters
    _samples   = 500_000

    def __new__(cls, a, /):
        return a.view(cls)

    def hist(self) -> str:
        edge = 0.005
        lines = 20
        a, median, b = np.quantile(self, [edge, 0.5, 1-edge])
        counts, bin_edges = np.histogram(self, range=(a, b), bins=lines, density=False)
        counts = np.array([edge, *(counts / self.size), edge])  # sums to 1
        percentages = np.cumsum(counts)
        bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
        bins = [' below', *[f'{edge:< .4g}' for edge in bin_midpoints], ' above']
        len_bin = max(len(b) for b in bins)
        bars = (counts / counts.max() * self._max_width).astype(int)
        lines = [f'{p:6.1%} | {b:<{len_bin}} | {'▒' * bar}' for p, b, bar in zip(percentages, bins, bars)]
        median_position = np.searchsorted(bin_edges, median)
        lines[median_position] += f'  ({median = })'
        return '\n'.join(reversed(lines))

    def __str__(self): return repr(self)
    def __repr__(self): 
        if self.dtype == 'bool':
            t = self.sum() / self.size
            f = 1 - t
            return f'True  | {t:6.1%} | {'▒' * int(self._max_width * t / max(t, f))}\n' +\
                   f'False | {f:6.1%} | {'▒' * int(self._max_width * f / max(t, f))}'
        a, b = np.quantile(self, [0.5, 0.95])
        if np.allclose(a, b):  # likely a single number
            return repr((a + b) / 2)
        return f'{a:.4g}~{b:.4g}\n\n' + self.hist()


class r(hist):
    '''PERT distrubution'''
    def __new__(cls, a, b, c, /):
        if a > c: a, c = c, a
        assert a <= b <= c
        lamb = 4
        r = c - a
        alpha = 1 + lamb * (b - a) / r
        beta = 1 + lamb * (c - b) / r
        data = a + np.random.beta(alpha, beta, cls._samples) * r
        return data.view(cls)


class n(hist):
    '''Normal distribution'''
    def __new__(cls, a, b, /):
        zscore = 2 * 1.64  # this determines the percentage of values between `a` and `b`
        mean = (a + b) / 2
        std = np.abs(a - b) / zscore
        data = np.random.normal(mean, std, cls._samples)
        return data.view(cls)


class u(hist):
    '''Uniform distribution'''
    def __new__(cls, a, b, /):
        data = np.random.uniform(min(a, b), max(a, b))
        return data.view(cls)
