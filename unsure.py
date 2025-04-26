import numpy as np
class r(np.ndarray):
    '''
    r(a, b): 90% sure item is between a and b
    r(np.array): convert from an array of random samples. size must match r._samples to interact with other ranges
    inherits np.ndarray, so you can use any numpy operations (exp, quantile, std, ...)  on this object.

    example usage:
    >>> r(1400,1700) * r(0.55,0.65) - r(600,700) - r(100,200) - 30 - 20
    
    -56.76~220.8
    
    100.0% |  above | ▒▒▒▒▒▒
     98.5% |  258   | ▒▒▒▒
     97.5% |  239.7 | ▒▒▒▒▒▒
     96.0% |  221.4 | ▒▒▒▒▒▒▒▒▒
     93.9% |  203   | ▒▒▒▒▒▒▒▒▒▒▒▒▒
     91.0% |  184.7 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     87.0% |  166.4 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     82.0% |  148   | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     75.8% |  129.7 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     68.7% |  111.4 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     60.6% |  93.03 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     52.1% |  74.69 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  (median = 79.42860413894547)
     43.5% |  56.36 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     35.1% |  38.02 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     27.3% |  19.69 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     20.5% |  1.357 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     14.8% | -16.98 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     10.2% | -35.31 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
      6.8% | -53.64 | ▒▒▒▒▒▒▒▒▒▒▒
      4.3% | -71.98 | ▒▒▒▒▒▒▒
      2.6% | -90.31 | ▒▒▒▒
      1.5% |  below | ▒▒▒▒▒▒

    >>> g = r(0,100)
    >>> (g>0) & (g<100)
    True  |  90.0% | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    False |  10.0% | ▒▒▒▒
    
    for more information see Unsure Calculator https://filiph.github.io/unsure/
    '''
    _max_width = 40  # max bar width in characters
    # _samples = 1_000_000
    _samples =   250_000
    def __new__(cls, a: float | np.ndarray, b: float | None = None, /):
        if isinstance(a, np.ndarray):
            data = a
        else:
            zscore = 2 * 1.64  # this determines the probability of values being between `a` and `b`
            mean = (a + b) / 2
            std = np.abs(a - b) / zscore
            data = np.random.normal(mean, std, cls._samples)
        return data.view(cls)

    def hist(self) -> str:
        edge = 0.015
        a, median, b = np.quantile(self, [edge, 0.5, 1-edge])
        counts, bin_edges = np.histogram(self, range=(a, b), bins=20, density=False)
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
            f = 1-t
            return f'True  | {t:6.1%} | {'▒' * int(self._max_width * t)}\n' +\
                   f'False | {f:6.1%} | {'▒' * int(self._max_width * f)}'
        q5, q95 = np.quantile(self, [0.05, 0.95])
        if np.allclose(q5, q95):  # likely a single number
            return repr((q5 + q95) / 2)
        return f'{q5:.4g}~{q95:.4g}\n\n' + self.hist()
