import os
import numpy as np
import matplotlib.pyplot as plt
import json

dt_string = "10-12-00-49-33"

num_particles = 1000

lengths = []
dEdDs = []
all_energies = []
all_lengths = []
for datafile in os.listdir('data'):
    if dt_string in datafile:
        filepath = os.path.join('data', datafile)
        
        print('will get data from', filepath)

        with open(filepath) as f:
            data_pair = json.load(f)
            
            vvolt1 = data_pair['1']['vacuum_level']
            vvolt2 = data_pair['2']['vacuum_level']
            
            d1 = (7.17-vvolt1)/6.02 * 4.5
            d2 = (7.17-vvolt2)/6.02 * 4.5
            
            print(d1,d2)
            energies1 = data_pair['1']['particle_energies']
            energies2 = data_pair['2']['particle_energies']
            
            # only if not empty
            if energies1 and energies2:
                
                total_energy1 = sum(energies1)
                total_energy2 = sum(energies2)
                
                dEdD =(total_energy1 - total_energy2)/(d2-d1)/len(energies1)
                d = (d1+d2)/2
                
                dEdDs.append(dEdD)
                lengths.append(d)
                

# do this to remove outliers from expected braggs curve         
# lengths.pop(0)
# lengths.pop(3)
# lengths.pop(6)
# dEdDs.pop(0)
# dEdDs.pop(3)
# dEdDs.pop(6)

plt.scatter(lengths, dEdDs)

plt.title("energy loss per particle per cm vs path length")
plt.xlabel("path length")
plt.ylabel("energy loss per particle per cm")

# fit a polynomial to the curve
for degree in range(6):
    z = np.polyfit(lengths, dEdDs, degree)
    p = np.poly1d(z)

    x = np.arange(min(lengths), max(lengths), 0.01)
    y = p(x)
    plt.plot(x,y, label=f'degree={degree}')
plt.legend()

plt.savefig('plots/braggs_curve_fit.png') 
        