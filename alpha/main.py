import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scripts.ReadMM import getMMVoltage
from scripts.ScopeTraceCapture import getScopeReading
from scripts.ControlVacuum import controlVacuum
from scripts.TriggerPulseDetection import countTriggers
from scripts.ReadScopeVoltage import getVoltage
from datetime import datetime
import time

ALPHA_CHARGE = 2
print('\n\n\n\n\n\n\n')

particle_counts = []
vacuum_voltages = []
particle_energies = []

trigger_time = 1
scope_trials = 1
mm_trials = 1

vacuum_level = float(getMMVoltage())
iteration = 0

now = datetime.now()
dt_string = now.strftime("%m-%d-%H-%M-%S")
while vacuum_level > 1.2:
    print(f'Starting iteration {iteration}')
    iteration += 1
    
    plt.clf()
    vacuum_level = 0
    for i in range(mm_trials):
        multimeter_voltage = float(getMMVoltage())
        vacuum_level += multimeter_voltage
    vacuum_level /= mm_trials
    print('vacuum level: ', vacuum_level)
    
    scope_trials = 1
    averaged_times = []
    averaged_voltages = []
    pp_voltage = 0
    for i in range(scope_trials):
        # vmin, vmax = getScopeReading(save=False)
        vmin, vmax = getVoltage()
        time.sleep(0.1)
        pp_voltage += vmax-vmin
    pp_voltage /= scope_trials 
    energy = round(pp_voltage * ALPHA_CHARGE, 4)
    print('energy:', energy)
    
    num_particles = countTriggers(trigger_time)
    print('num particles: ', num_particles)

    vacuum_voltages.append(vacuum_level)
    particle_counts.append(num_particles)
    particle_energies.append(energy)
    
    opentime = 0.1
    controlVacuum(roomvalve=opentime)

vacuum_voltages = np.array(vacuum_voltages)
particle_counts = np.array(particle_counts)
particle_energies = np.array(particle_energies)

plt.clf()
plt.scatter(vacuum_voltages, particle_counts)
plt.xlabel("vacuum voltages")
plt.ylabel(f'particle counts in {trigger_time}s')
plt.title('vacuum vs counts')
plt.savefig(f'plots/{dt_string}-counts.png')

plt.clf()
plt.title('vacuum vs energies')
plt.xlabel("vacuum voltages")
plt.ylabel('particle energy')
plt.scatter(vacuum_voltages, particle_energies)
plt.savefig(f'plots/{dt_string}-energy (avg of {scope_trials}).png')

plt.clf()
plt.title('energies vs counts')
plt.xlabel("particle energy")
plt.ylabel('particle count')
plt.scatter(particle_energies, particle_counts)
plt.savefig(f'plots/{dt_string}-energy-vs-count.png')

np.save(f'data/{dt_string}-vvolts.npy', vacuum_voltages)
np.save(f'data/{dt_string}-energies.npy', particle_energies)
np.save(f'data/{dt_string}-counts.npy', particle_counts)
    

# USB0::6833::1303::DS1ZE231705963::0::INSTR