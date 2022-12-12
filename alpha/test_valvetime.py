from scripts.ControlVacuum import controlVacuum
import numpy as np
import matplotlib.pyplot as plt
from scripts.ReadMM import getMMVoltage
from scripts.getValveTime import getRoomvalveTime
import matplotlib.pyplot as plt

targets = [7.15, 7.05, 6.55, 6.45, 5.55, 5.45, 5.3, 5.2, 5.05, 4.95, 4.8, 4.7, 4.55, 4.45, 4.3, 4.2, 4.05, 3.95, 3.8, 3.7, 3.55, 3.45, 3.05, 2.95]
actual = []

i = 0
while(i < len(targets)):
    
    vacuum_level = float(getMMVoltage())
    target_level = targets[i]
    
    dt = getRoomvalveTime(vacuum_level, target_level)
    controlVacuum(roomvalve=dt)
    
    new_level = float(getMMVoltage())
    
    actual.append(new_level)
    print('level = ', vacuum_level, 'opened for ', dt, 's\nnew level = ', new_level, '\n\n')
    i += 1
    

plt.plot(np.arange(len(targets)) + 1, targets, label="targets")
plt.plot(np.arange(len(targets)) + 1, actual, label="actual")
plt.ylabel("voltage")
plt.legend()
plt.savefig("test_valve_wait.png")    