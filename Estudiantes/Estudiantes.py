import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
 
X = ss.norm(50,10)
print(((X.cdf(70) - X.cdf(60))*215)+22)
print((X.cdf(65) - X.cdf(55))*110)
