from click import format_filename
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import json

filepath = "data/10-12-00-49-33-V=7_10.json"

with open(filepath) as f:
    data_pair = json.load(f)


    energies = np.array(data_pair['1']['particle_energies'])

    print(np.mean(energies))