import numpy as np
class hist(np.ndarray):
    '''Base class for distributions. plots a histogram'''
    max_width = 40  # max bar width in characters
    samples   = 500_000

    def __new__(cls, a, /):
        return a.view(cls)

    def hist(self, bins=20) -> str:
        edge = 0.005
        a, median, b = np.quantile(self, [edge, 0.5, 1-edge])
        counts, bin_edges = np.histogram(self, range=(a, b), bins=bins, density=False)
        counts = np.array([edge, *(counts / self.size), edge])  # sums to 1
        percentages = np.cumsum(counts)
        bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
        bins = [' below', *[f'{edge:< .4g}' for edge in bin_midpoints], ' above']
        len_bin = max(len(b) for b in bins)
        bars = (counts / counts.max() * self.max_width).astype(int)
        lines = [f'{p:6.1%} | {b:<{len_bin}} | {'▒' * bar}' for p, b, bar in zip(percentages, bins, bars)]
        median_position = np.searchsorted(bin_edges, median)
        lines[median_position] += f'  ({median = })'
        return '\n'.join(reversed(lines))

    def bool_hist(self) -> str:
        t = self.sum() / self.size
        f = 1 - t
        return f'True  | {t:6.1%} | {'▒' * int(self.max_width * t / max(t, f))}\n' +\
               f'False | {f:6.1%} | {'▒' * int(self.max_width * f / max(t, f))}'

    def __str__(self): return repr(self)
    def __repr__(self): 
        if self.dtype == 'bool':
            return self.bool_hist()
        a, b = np.quantile(self, [0.5, 0.95])
        if np.allclose(a, b):  # likely a single number
            return repr((a + b) / 2)
        return f'{a:.4g}~{b:.4g}\n\n' + self.hist()


class r(hist):
    '''PERT distrubution'''
    def __new__(cls, a, b, c, /):
        if a > c: a, c = c, a
        assert a <= b <= c
        w = 4  # mean = (a + b*w + c) / (2 + w)
        r = c - a
        alpha = 1 + w * (b - a) / r
        beta = 1 + w * (c - b) / r
        data = a + np.random.beta(alpha, beta, cls.samples) * r
        return data.view(cls)


class n(hist):
    '''Normal distribution'''
    def __new__(cls, a, b, /):
        zscore = 2 * 1.64  # this determines the percentage of values between `a` and `b`
        mean = (a + b) / 2
        std = np.abs(a - b) / zscore
        data = np.random.normal(mean, std, cls.samples)
        return data.view(cls)


class u(hist):
    '''Uniform distribution'''
    def __new__(cls, a, b, /):
        data = np.random.uniform(min(a, b), max(a, b), cls.samples)
        return data.view(cls)
