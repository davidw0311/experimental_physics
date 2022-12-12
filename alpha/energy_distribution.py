import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scripts.ReadMM import getMMVoltage
from scripts.ScopeTraceCapture import getScopeReading
from scripts.ControlVacuum import controlVacuum
from scripts.TriggerPulseDetection import countTriggers
from scripts.ReadScopeVoltage import getVoltage
import time
from datetime import datetime

import time
ALPHA_CHARGE = 2
print('\n\n\n\n\n\n\n')

particle_counts = []
vacuum_voltages = []
particle_energies = []

scope_trials = 1000
mm_trials = 1
trigger_time = 10
count = 0
vacuum_level = float(getMMVoltage())

it = 0 
now = datetime.now()
dt_string = now.strftime("%m-%d-%H-%M-%S")
trigger_level = 0.5 #500 mV

while vacuum_level > 2:
    print('iteration: ', it)
    it += 1
    vacuum_level = float(getMMVoltage())
        
    particle_energies = []
    prev_energy = 0
    i = 0
    pbar = tqdm(total = scope_trials)
    while i < scope_trials:
        vmin, vmax = getVoltage(trigger_level)
        pp_voltage = vmax-vmin
        energy = pp_voltage * ALPHA_CHARGE
        print('energy', energy)

        if energy > 0 and energy < 20:
            pbar.update(1)
            particle_energies.append(energy)
            prev_energy = energy
            i += 1    
        time.sleep(0.1)
        
    plt.clf()
    plt.hist(particle_energies, bins=max(10, int(len(particle_energies)/20)))
    plt.title(f"energy histogram ({scope_trials} particles) for vacuum level = {vacuum_level}\ncounts in {trigger_time}s = {particle_counts}", wrap=True)
    plt.xlabel("energy (MeV)")
    plt.ylabel("count")
    plt.savefig(f"plots/{dt_string}-energy-distr-vac={vacuum_level}.png")
    
    particle_energies_np = np.array(particle_energies)
    np.save(f'data/{dt_string}-energy-clusters-{vacuum_level}.npy', particle_energies_np)
    print(f'{dt_string}-{vacuum_level} saved!')
    
    controlVacuum(roomvalve=2)
    vacuum_level = float(getMMVoltage())





# USB0::6833::1303::DS1ZE231705963::0::INSTR