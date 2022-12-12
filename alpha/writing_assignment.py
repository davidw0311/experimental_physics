import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import json

from scipy.stats import norm


dt_string = "10-12-00-49-33"
plt.clf()

all_data = []
for datafile in os.listdir("data"):
    if dt_string in datafile:
        filepath = os.path.join('data', datafile)
        
        print('will get data from', filepath)
        all_data.append(filepath)

count = 0
colors = ['b','r','g','y']   
   
for filepath in sorted(all_data, reverse=True):
    with open(filepath) as f:
        data_pair = json.load(f)
        
        for i in (1,2):
            vvolt = data_pair[str(i)]['vacuum_level']
            counts = data_pair[str(i)]['particle_counts']
            d = (7.17-vvolt)/6.02 * 4.5

            if vvolt in [7.141399, 6.076519, 5.325791, 4.049926]:
                energies = np.array(data_pair[str(i)]['particle_energies'])

                bin_size = 0.075

                fenergies = energies[energies < 15]

        
                
                n, bins, patches = plt.hist(fenergies, bins=np.arange(2.0, 10.0, bin_size), label = f"Vacuum Level = {vvolt:.3}V",color=colors[count], alpha=0.4)
                (mu, sigma) = norm.fit(fenergies)
                y = norm.pdf(bins,mu,sigma)
               
                y = y*len(fenergies)*np.diff(bins)[0]
                
                plt.plot(bins, y, '--',color=colors[count], linewidth=2)
                
                count += 1
                
                print(mu, sigma)
                
                
                

plt.title(f"Energy Histogram of alpha particles detected in 10s at different Vacuum Levels", size=10, y=1.)
plt.xlim(2,10)
plt.ylim(0, 100)
plt.xlabel("Energy (MeV)")
plt.ylabel("Particle counts")
plt.legend()   
plt.tight_layout()                
name = f"writing_assignment/all.png"
if not os.path.exists(f'writing_assignment/{dt_string}'):
    os.makedirs(f'writing_assignment/{dt_string}')
plt.savefig(name)

print('saved!!')