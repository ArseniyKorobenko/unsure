# unsure
numpy-powered version of [Unsure Calculator](https://filiph.github.io/unsure/)  
for use in jupyter notebooks and python repls

python doesn't let you define custom operators on builtin types so here it's just a normal class constructor.  

r(min, mode, max): PERT distribution (recommended), takes the mininum, most likely, and maximum value  
n(a, b): normal distribution, 90% confidence values are between `a` and `b`  
u(a, b): uniform distribution between `a` and `b`  

hist(np.array): convert from an array of random samples. size should match hist._samples to interact with other distrubutions  
distributions inherit np.ndarray, so you can use any array operations on these objects (np.exp, np.std, np.quantile, plt.hist, sns.kdeplot, etc)

example usage:
```py
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
```
for more information see Unsure Calculator at https://filiph.github.io/unsure/  
