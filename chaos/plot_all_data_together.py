
from dataclasses import dataclass
import os
import numpy as np
import matplotlib.pyplot as plt
import re

# dt_string = '10-20-15-50-41'
# dt_string = '10-21-02-09-22'
dt_string = '10-28-01-07-45'
lastN = 100
all_data_files = []
for file in os.listdir("data"):
    if dt_string in file:
        all_data_files.append("data/"+file)

all_data_files = sorted(all_data_files)

all_data_array = np.array([])
all_data_array_lastN = np.array([])
valve_levels = np.array([])

for datafile in all_data_files:
    print(datafile)
    data = np.load(datafile)
    data = data[data>0]
    data = data[data<np.mean(data)*5]
    # data = data[-50:]
    all_data_array = np.concatenate((all_data_array,data),0)
    all_data_array_lastN = np.concatenate((all_data_array_lastN,data[-lastN:]),0)
    # plt.scatter(data)
    valve_level = int(re.split('[_.=-]',datafile)[-4])
    valve_level_arr = np.array([valve_level]*len(data[-lastN:]))
    valve_levels = np.concatenate((valve_levels,valve_level_arr),0)

plt.scatter(valve_levels, all_data_array_lastN, s=0.1, color='b')    
plt.title(f'Last {lastN} Tn for each level vs valve level')
plt.xlabel('Valve Level')
plt.ylabel('Tn')
plt.tight_layout()
plt.savefig(f"{dt_string}-point-data.png")
plt.clf()
plt.title("All Tn as continuous array")   
plt.xlabel('Drop number')
plt.ylabel('Tn') 
plt.scatter(np.arange(len(all_data_array)), all_data_array, s=3)
plt.tight_layout()
plt.savefig(f'{dt_string}-data-bifurcation.png')