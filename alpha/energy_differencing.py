import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scripts.ReadMM import getMMVoltage
from scripts.ScopeTraceCapture import getScopeReading
from scripts.ControlVacuum import controlVacuum
from scripts.TriggerPulseDetection import countTriggers
from scripts.getValveTime import getRoomvalveTime

import time
from datetime import datetime

from xml.sax import default_parser_list
import numpy as np
import sys
import pyvisa as visa
from matplotlib import pyplot as plt
import argparse
import time

import time
import json


def getVoltage(trigger_level=None):
    # Make the pyvisa resource manager
    rm = visa.ResourceManager()
    # Get the USB device, e.g. 'USB0::0x1AB1::0x0588::DS1ED141904883'
    instruments = rm.list_resources()
    usbs = list(filter(lambda x: 'USB' in x, instruments))
    # print(usbs)
    scope_address = ""
    for address in usbs :
        if "::DS" in address :
            scope_address = address
    if not scope_address :
        print("Could not find address of scope!")
        exit(1)

    # print("Will open instrument",scope_address)

    scope = rm.open_resource(scope_address, timeout=2000, chunk_size=1024000)

    if trigger_level:
        scope.write(":TRIG:EDG:LEV {0}".format(trigger_level))
        
    vmin = float(scope.query(":MEAS:VMIN?").strip())
    vmax = float(scope.query(":MEAS:VMAX?"))
    rm.close()
    scope.close()
    return vmin, vmax

ALPHA_CHARGE = 2
print('\n\n\n\n\n\n\n')

trigger_time = 10
trigger_level = 0.5 #mV

now = datetime.now()
dt_string = now.strftime("%m-%d-%H-%M-%S")
# dt_string = "10-12-00-49-33"
# target_voltages = [5.25, 5, 4.75, 4.5, 4.25, 4, 3.75, 3.5, 3]
target_voltages = [4.3, 4.1, 3.9, 3.7]

vacuum_level = float(getMMVoltage())

# make sure we start at higher than the first voltage
assert(vacuum_level > target_voltages[0]), f"the chamber is not at high enough vacuum to start the experiment!\nCurrent voltage = {vacuum_level}"
it = 0 
for voltage_level in target_voltages:
    print('iteration: ', it)
    it += 1
    
    print('\n\nGetting Pair of Measurements:\n--------------------------')
    data_dict = {1:{}, 2:{}}
    pair_level = 'V={:.2f}'.format(voltage_level).replace(".","_")
    
    for i, dV in enumerate([0.02, -0.02]): # get pairs of measurements for differencing
        j = i + 1 # use 1 indexing
        
        vacuum_level = float(getMMVoltage())
        
        dt = getRoomvalveTime(vacuum_level, voltage_level + dV)
        controlVacuum(roomvalve=dt)
        vacuum_level = float(getMMVoltage()) # acheive desired voltage
        
        particle_counts = countTriggers(trigger_time)
        print(f'{particle_counts} particles counted in {trigger_time}s at {vacuum_level}V')
        
        # particle_counts = 3
        
        particle_energies = []
        i = 0
        pbar = tqdm(total = particle_counts)
        while i < particle_counts:
            vmin, vmax = getVoltage()
            pp_voltage = vmax-vmin
            energy = pp_voltage * ALPHA_CHARGE

            if energy > 0 and energy < 20: # to avoid noisy measurements
                pbar.update(1)
                particle_energies.append(energy)
                i += 1   
             
        # save data
        data_dict[j]['vacuum_level'] = vacuum_level
        data_dict[j]['trigger_time'] = trigger_time
        data_dict[j]['particle_counts'] = particle_counts
        data_dict[j]['particle_energies'] = particle_energies
        
        # Serializing json
        json_object = json.dumps(data_dict, indent=4)
        
        # save file
        datafile = f"data/{dt_string}-{pair_level}.json"
        with open(datafile, "w") as outfile:
            outfile.write(json_object)
        print(f'{datafile} saved!')
        





# USB0::6833::1303::DS1ZE231705963::0::INSTR