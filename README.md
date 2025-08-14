# unsure
numpy-powered version of [Unsure Calculator](https://filiph.github.io/unsure/) (unofficial)  
intended for use in jupyter notebooks and python repls, but also works well with print() in scripts.

r(min, mode, max): PERT distribution (recommended), takes the mininum, most likely, and maximum value  
n(a, b): normal distribution, 90% confidence values are between `a` and `b`  
u(a, b): uniform distribution between `a` and `b`  

hist(np.array): convert from an array of random samples. size should match hist.samples to broadcast with other distrubutions  

distributions inherit np.ndarray, so you can use all the usual array operations on these objects (np.exp, np.std, np.quantile, plt.hist, sns.kdeplot, etc), or call np.array() to get the underlying data  
see unsure.py for how to define your own custom distribution

example usage:
```py
>>> r(1400,1500,1700) * r(0.55,0.60,0.65) - r(600,620,700) - r(100,120,200) - 30 - 20

18.9~184.3  # (this is the 90% confidence window)

100.0% |  above | ▒▒
 99.5% |  223   | ▒▒
 98.9% |  210.4 | ▒▒▒▒
 97.9% |  197.8 | ▒▒▒▒▒▒
 96.3% |  185.3 | ▒▒▒▒▒▒▒▒▒▒
 93.8% |  172.7 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 90.2% |  160.1 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 85.4% |  147.5 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 79.2% |  134.9 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 71.6% |  122.3 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 62.9% |  109.7 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 53.4% |  97.13 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  (median = 99.07301)
 43.6% |  84.54 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 34.1% |  71.95 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 25.4% |  59.36 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 17.9% |  46.77 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 11.9% |  34.18 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  7.4% |  21.59 | ▒▒▒▒▒▒▒▒▒▒▒▒
  4.2% |  8.999 | ▒▒▒▒▒▒▒▒
  2.3% | -3.591 | ▒▒▒▒
  1.1% | -16.18 | ▒▒
  0.5% |  below | ▒▒

>>> g = r(0,50,100)
>>> (g>20) & (g<40)
True  |  26.0% | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
False |  74.0% | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
```
for more information see Unsure Calculator at https://filiph.github.io/unsure/  
