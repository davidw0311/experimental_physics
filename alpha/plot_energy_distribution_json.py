from click import format_filename
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import json

dt_string = "10-12-00-49-33"

for datafile in os.listdir("data"):
    if dt_string in datafile:
        filepath = os.path.join('data', datafile)
        
        print('will get data from', filepath)

        with open(filepath) as f:
            data_pair = json.load(f)
            
            for i in (1,2):
                vvolt = data_pair[str(i)]['vacuum_level']
                counts = data_pair[str(i)]['particle_counts']
                d = (7.17-vvolt)/6.02 * 4.5
            
                energies = np.array(data_pair[str(i)]['particle_energies'])

                plt.clf()
                num_bins = 50

                fenergies = energies[energies < 15]

                plt.hist(fenergies, bins=np.arange(2, 10, 0.1))
                plt.title(f"energy histogram for vacuum level = {vvolt}, #alphas = {counts}")
                plt.xlim(2,10)
                plt.ylim(0, 140)
                plt.xlabel("energy (MeV)")
                plt.ylabel("count")
                
                if not os.path.exists(f'good_plots/{dt_string}'):
                    os.makedirs(f'good_plots/{dt_string}')
                    
                name = f"good_plots/{dt_string}/{dt_string}-energy-distr-vac={vvolt}.png"
                plt.savefig(name)

                print('saved!!', name)