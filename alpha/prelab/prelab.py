import numpy as np
import matplotlib.pyplot as plt
import os

num_particles = 100000
E0 = 28.8
stdv = 2
particles = np.random.normal(loc=E0, scale=2, size=num_particles)

plt.hist(particles, bins=1000)
plt.title(f'Initial distribution of {num_particles} particles centered at {E0}MeV')
plt.xlabel("Energy of Particle (MeV)")
plt.ylabel("Count")
plt.savefig('initial_distribution')

def simulate_single_passage(particles, dE, Ethresh = 0.1):
    
    # fraction F of particles lose energy dE
    F = dE/E0 # some relationship for F 
    
    # random particles get chosen to lose dE energy
    rand_indices = np.random.choice(len(particles), int(num_particles*F), replace=False)
    particles[rand_indices] -= dE
    
    particles = particles[particles>Ethresh]
    return particles

def plot_energy_distribution(particles, it, dE, total_it):
    plt.clf()
    plt.hist(particles, bins=1000)
    plt.title(f'Energy distribution, iteration: {it}')
    plt.xlabel("Energy of Particle (MeV)")
    plt.ylabel("Count")
    name = f'energy_loss_{total_it}iterations_dE{dE}'
    if not os.path.exists(name):
        os.makedirs(name)
    plt.savefig(f'{name}/it{it}.png')


# simulate N passings
dE = 6
total_it = 20
for it in range(1,total_it+1):
    print(f'iteration: {it}')
    particles = simulate_single_passage(particles, dE) 
    plot_energy_distribution(particles, it, dE, total_it)
