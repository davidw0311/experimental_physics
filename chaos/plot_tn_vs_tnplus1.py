import os
import numpy as np
import re
import matplotlib.pyplot as plt 

'''
makes figures for Tn vs Tn+1 of a certain timestamp
'''

# dt_string = '10-20-15-50-41'
# dt_string = '10-21-02-09-22' # 1k pts
# dt_string = '10-28-01-07-45' # 5k pts
dt_string = '10-29-01-46-32' # valve level 306 long term
dt_string = '00-00-00-00-00' # simulated

all_data_files = []
for file in os.listdir("data"):
    if dt_string in file:
        all_data_files.append("data/"+file)
       

for df in all_data_files:
    print(df)
    drips = np.load(df)
    drips = drips[drips > 0]
    drips = drips[drips < np.mean(drips)*5]
    # valve_level = df[df.find('valve_level')+len('valve_level')]
    # valve_level = int(re.split('[.=-]',df)[-3])
    
    valve_level = int(re.split('[._=-]',df)[-4])
    print(valve_level)
    plot_name = f'plots/2d/{dt_string}-valve_level={valve_level:03}.png'
    tn = drips[:-1]
    tnp1 = drips[1:]

    plt.clf()
    plt.scatter(tn, tnp1)
    plt.xlabel('Tn')
    plt.ylabel('Tn + 1')
    plt.title(f"valve lv = {valve_level}", fontsize=40)
    plt.tight_layout()
    plt.savefig(plot_name)
    
    
    
    
    
    