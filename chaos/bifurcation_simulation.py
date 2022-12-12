import numpy as np
import matplotlib.pyplot as plt

# simualate the bifurcation diagram

plt.rcParams["figure.figsize"] = [20, 10]
ps = []
all_x = []

for p in np.arange(0,4,0.001):
    x = np.random.rand()
    for i in range(1000):
        x = p*x*(1-x)
    xs = []
    for i in range(5000):
        x = p*x*(1-x)
        xs.append(x)

    last_length=500
    all_x += xs[-last_length:]
    ps += [p] * last_length
    
plt.scatter(np.arange(len(all_x)),all_x,s=0.001)
plt.savefig('bifurcation.png')