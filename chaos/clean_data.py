import os
import numpy as np
import re
dt_string = '10-20-15-50-41'
all_data_files = []
for file in os.listdir("data"):
    if dt_string in file:
        all_data_files.append("data/"+file)

for datafile in all_data_files:
    data = np.load(datafile)
    level = int(re.split('[=_]',datafile)[2])
    dataname = f'{dt_string}-valve_level={level:03}-1000dp.npy'
    print(dataname)
    os.remove(datafile)

    np.save(dataname, data)
