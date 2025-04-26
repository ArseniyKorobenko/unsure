# unsure
numpy-powered version of [Unsure Calculator](https://filiph.github.io/unsure/)  
For use in jupyter notebooks and python repls

python doesn't let you define custom operators on builtin types so here it's just a normal class.  
r(a, b): 90% sure item is between a and b  
r(np.array): convert from an array of random samples. size must match r._samples to interact with other ranges  
inherits np.ndarray, so you can use any numpy operations (exp, quantile, std, ...)  on this object.
## example usage:
```py
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
```
for more information see Unsure Calculator at https://filiph.github.io/unsure/
