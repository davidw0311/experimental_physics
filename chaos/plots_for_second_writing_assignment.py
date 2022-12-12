import os
import numpy as np
import re
import matplotlib.pyplot as plt 
import textwrap 
'''
makes figures for Tn vs Tn+1 of a certain timestamp
'''

LEVEL = 317
# dt_string = '10-20-15-50-41'
dt_string = '10-21-02-09-22' # 1k pts
# dt_string = '10-28-01-07-45' # 5k pts
# dt_string = '10-29-01-46-32' # valve level 306 long term
# dt_string = '00-00-00-00-00' # simulated

all_data_files = []
for file in os.listdir("data"):
    if dt_string in file:
        all_data_files.append("data/"+file)
       

for df in all_data_files:
    
    # drips = drips[drips > 0]
    # drips = drips[drips < np.mean(drips)*5]
    # drips = drips[::-1]
    # valve_level = df[df.find('valve_level')+len('valve_level')]
    # valve_level = int(re.split('[.=-]',df)[-3])
    
    valve_level = int(re.split('[._=-]',df)[-4])
    
    if valve_level == LEVEL:
        drips = np.load(df)
        print(valve_level)
        plot_name = f'writing_assignment_plots/{dt_string}-valve_level={valve_level:03}.png'
        tn = drips[:-1]
        tnp1 = drips[1:]

x = np.random.rand()
p = 3.6
zeta = 0.02
for i in range(1000):
    x = p*x*(1-x) + zeta*np.random.normal()

xs = []
for i in range(1000):
    x = p*x*(1-x) + zeta*np.random.normal()
    xs.append(x)

xs = np.array(xs)
xs = -xs
xn = xs[:-1]
xnp1 = xs[1:]   


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 10))
# title = "\n".join(textwrap.wrap("Chaotic behaviour of drips at valve level = 319 compared to negative 1-D logistic map with noise", 50))
# plt.suptitle(title, fontsize=15)

plt1 = axes[0][0]
plt1.scatter(np.arange(len(drips)), drips, s=1)
plt1.ticklabel_format(style='sci',scilimits=(-5,5),axis='both')
plt1.set_ylabel("Drip Rate (us)")
plt1.set_xlabel("Drop number")
plt1.set_title(f"A")

plt2 = axes[0][1]
plt2.scatter(np.arange(len(xs)), xs, s=1, color='green')
plt2.set_title("B")
plt2.set_xlabel("Drop number")
plt2.set_ylabel("xn")
# plt2.set_yticks([])

plt3 = axes[1][0]
plt3.scatter(tn, tnp1, s=1)
plt3.set_xlabel("Tn")
plt3.set_ylabel("Tn + 1")
plt3.ticklabel_format(style='sci',scilimits=(-2,3),axis='both')
plt3.set_title(f"C")

plt4 = axes[1][1]
plt4.scatter(xn, xnp1, s=1, color='green')
# plt4.set_xticks([])
# plt4.set_yticks([])
plt4.set_xlabel("xn")
plt4.set_ylabel("xn + 1")
plt4.set_title(f"D")
fig.tight_layout()


# plt.subplot
# plt.clf()

# plt.scatter(tn, tnp1)
# # plt.plot(tn, tnp1)
# plt.xlabel('Tn')
# plt.ylabel('Tn + 1')
# plt.ticklabel_format(style='sci',scilimits=(-2,3),axis='both')
# plt.title(f"valve lv = {valve_level}", fontsize=40)
# plt.tight_layout()
# plt.savefig(plot_name)
        

# plt.clf()


# tn = -tn + 2*np.mean(tn)
# tnp1 = -tnp1 + 2*np.mean(tnp1)

# midxn = (np.max(xn)-np.min(xn))/2
# midtn = (np.max(tn)-np.min(tn))/2
# midxnp1 = (np.max(xnp1)-np.min(xnp1))/2
# midtnp1 = (np.max(tnp1)-np.min(tnp1))/2

# xn = xn*( np.max(tn)-np.min(tn) )/(np.max(xn)-np.min(xn)) + np.mean(tn)-np.mean(xn) - 0.05e5
# xnp1 = xnp1*(np.max(tnp1)-np.min(tnp1))/(np.max(xnp1)-np.min(xnp1)) + np.mean(tnp1)-np.mean(xnp1) - 0.03e5
# xn = xn * (midtn/midxn) + midtn-midxn
# xnp1 = xnp1 * (midtnp1/midxnp1) + midtnp1-midxnp1



# plt.scatter(xn, xnp1, color='red')
# plt.scatter(tn,tnp1 )
# plt.ticklabel_format(style='sci',scilimits=(-2,3),axis='both')
plt.savefig("writing_assignment_plots/model.png")
    
    
    
    