import os
import numpy as np
import re
import matplotlib.pyplot as plt 

'''
makes figures for all the data of a certain timestamp
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
    plot_name = f'plots/3d/{dt_string}-valve_level={valve_level:03}.png'
    tn = drips[:-2]
    tnp1 = drips[1:-1]
    tnp2 = drips[2:]
    plt.clf()
    ax = plt.axes(projection='3d')

    ax.scatter3D(tn, tnp1, tnp2)
    ax.set_xlabel('T n')
    ax.set_ylabel('T n+1')
    ax.set_zlabel('T n+2')
    
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    plt.title(f"valve lv = {valve_level}", fontsize=40)
    plt.savefig(plot_name)
    
    
    
    
    
    