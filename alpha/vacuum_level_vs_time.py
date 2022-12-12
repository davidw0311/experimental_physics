from scripts.ControlVacuum import controlVacuum
import numpy as np
import matplotlib.pyplot as plt
from scripts.ReadMM import getMMVoltage

total_time = 0
times = []
vvolts = []

vacuum_level = float(getMMVoltage())

times.append(total_time)
vvolts.append(vacuum_level)

dt = 1
while vacuum_level > 1.5:
    controlVacuum(roomvalve=dt)
    vacuum_level = float(getMMVoltage())
    total_time += dt
    
    times.append(total_time)
    vvolts.append(vacuum_level)
    
    print('vacuum voltage: ', vacuum_level)
    print('valve opened for', total_time)
    

plt.scatter(times, vvolts)
# plt.plot(times, vvolts)
plt.xlabel('valve open (s)')
plt.ylabel('vacuum voltage')
plt.title('vacuum voltage vs time room valve opened')
plt.savefig('vvolt_vs_time.png')
np.save("vvolt_vs_time_times.npy", np.array(times))
np.save("vvolt_vs_time_vvolts.npy", np.array(vvolts))
