from click import format_filename
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os

# dt_string = "10-06-01-53-33"
dt_string = "10-06-01-06-55"

for datafile in os.listdir("data"):
    if dt_string in datafile:
        filename = "data/"+datafile
        particle_energies = np.load(filename)

        vacuum_level = float(filename.split('-')[-1][:-4])

        plt.clf()
        num_bins = 50

        fparticle_energies = particle_energies[particle_energies< 15]
        plt.hist(fparticle_energies, bins=np.arange(2, 10, 0.1))
        plt.title(f"energy histogram for vacuum level = {vacuum_level}")
        plt.xlim(2,10)
        plt.xlabel("energy (MeV)")
        plt.ylabel("count")
        
        if not os.path.exists(f'good_plots/{dt_string}'):
            os.makedirs(f'good_plots/{dt_string}')
            
        name = f"good_plots/{dt_string}/{dt_string}-energy-distr-vac={vacuum_level}.png"
        plt.savefig(name)
        np.save(f"good_plots/{dt_string}/{datafile}", particle_energies)
        print('saved!!', name)