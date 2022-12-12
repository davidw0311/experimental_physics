import numpy as np
import matplotlib.pyplot as plt

# simualate the bifurcation diagram


for p in np.arange(3.3,3.995,0.005):
    x = np.random.rand()
    for i in range(5000):
        x = p*x*(1-x)
    xs = []
    for i in range(5000):
        x = p*x*(1-x)
        xs.append(x)
    
    pnum = int(200*p)
    filename = f"data/00-00-00-00-00-valve_level={pnum:03}_5000-dps.npy"
    xs = np.array(xs)
    np.save(filename, xs)
    
    