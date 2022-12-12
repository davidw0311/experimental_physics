
import matplotlib.pyplot as plt
import numpy as np
import os

dt_string = '10-04-12-19-39'
#'10-03-21-07-01' 
dt_string = "10-06-16-54-17"

vacuum_voltages = np.load(f'data/{dt_string}-vvolts.npy')
particle_counts = np.load(f'data/{dt_string}-counts.npy')
particle_energies = np.load(f'data/{dt_string}-energies.npy')

indices = (particle_energies>2) & (particle_energies<20)
fvacuum_voltages = vacuum_voltages[indices]
fparticle_counts = particle_counts[indices]
fparticle_energies = particle_energies[indices]

if not os.path.exists(f'good_plots/{dt_string}'):
    os.makedirs(f'good_plots/{dt_string}')
plt.clf()
plt.scatter(fvacuum_voltages, fparticle_counts)
plt.xlabel("vacuum voltages")
plt.ylabel('particle counts')
plt.title('vacuum vs counts')
plt.savefig(f'good_plots/{dt_string}/{dt_string}-counts.png')

plt.clf()
plt.title('vacuum vs energies')
plt.xlabel("vacuum voltages")
plt.ylabel('particle energy')
plt.scatter(fvacuum_voltages, fparticle_energies)
plt.savefig(f'good_plots/{dt_string}/{dt_string}-energy.png')

plt.clf()
plt.title('energies vs counts')
plt.xlabel("particle energy")
plt.ylabel('particle count')
plt.scatter(fparticle_energies, fparticle_counts)
plt.savefig(f'good_plots/{dt_string}/{dt_string}-energy-vs-count.png')

np.save(f'good_plots/{dt_string}/{dt_string}-vvolts.npy', vacuum_voltages)
np.save(f'good_plots/{dt_string}/{dt_string}-counts.npy', particle_counts)
np.save(f'good_plots/{dt_string}/{dt_string}-energies.npy', particle_energies)
