from scripts.ReadPhotoGate import getDroprates
from scripts.ShutoffValve import controlSwitch
from stepcontrol import controlStepper
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%m-%d-%H-%M-%S")

controlSwitch(on=True)
time.sleep(2)

# reset to 0
valve_level = controlStepper(motor=2, step=10, stepspersec=10)
num_data_points = 5000
sleep_time = 1


starting_level = 340

dif = starting_level - valve_level
valve_level = controlStepper(motor=2, step=dif, stepspersec=10)
while valve_level >= 150:
    print(f'sleeping for {sleep_time} seconds')
    time.sleep(sleep_time)
    drop_rates = []
    # for i in range(100):
    dr = getDroprates(num_data_points)
    
    drop_rates = drop_rates + dr
    
    plt.clf()
    drnp = np.array(drop_rates)
    drnp = drnp[drnp>0]
    plt.scatter(np.arange(len(drnp)), drnp)
    plt.xlabel('step')
    plt.ylabel('time between successive drops (us)')
    plt.title(f"valve_level={valve_level}")
    plt.tight_layout()
    
    plt.savefig(f'plots/{dt_string}-valve_level={valve_level:03}.png')
    np.save(f'data/{dt_string}-valve_level={valve_level:03}_{num_data_points}-dps.npy', np.array(drop_rates))
    print("plot and data saved!")
    
    step_incr = -1
    # if valve_level < 100:
    #     step_incr = 20
    # elif valve_level < 200:
    #     step_incr = 10
    # else:
    #     step_inc = 5
        
    valve_level = controlStepper(motor=2, step=step_incr, stepspersec=10)
    
    
    
controlSwitch(on=False)