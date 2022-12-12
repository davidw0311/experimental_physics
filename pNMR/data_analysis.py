import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/nmr_data_nov_24/min_envelope_aw=12-16us.DAT', sep="\s+")
print(df['Time'])

plt.plot(df['Time'], df['Ch1'], label='Ch1', color="orange")
plt.plot(df['Time'], df['Ch2'], label='Ch2', color='lightblue')
plt.legend()
# plt.savefig('figures/resonant_signal_50.jpg')
plt.show()
