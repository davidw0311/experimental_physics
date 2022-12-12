# Chaos Lab

In this lab, we investigate the behaviour of chaotic system through measuring the drip rates of a "leaky faucet"

## Setting up
ssh into chaos server via vs code
ran 
```
ssh-keygen -t rsa -b 4096 -C "david311@student.ubc.ca"
```

and copied the id_rsa.pub into Github ssh keys

created a folder called scripts, and imported all the code from /usr/local/bin into here. Copied stepcontrol from /home/student/Stepper/stepcontrol.py

Will customize these scripts to help with measurement. 

## Custom code

#### Wrote the following scripts:

[stepcontrol.py](stepcontrol.py)

To automate the movement of the motors

[scripts/ShutoffValve.py](scripts/ShutoffValve.py)

Script to control switching on and off the valve

[plot_drip_number.py](plot_drip_number.py) 

For data collection. This runs an automated python script to collect a set number of datapoints for various valve levels. Each time the scrip is initialized, the current time-stamp is saved and used as an identifier for this run. All the data collected from the run is saved under [/data](/data) with the date-time string as it's identifier. All the data collected for this experiment can be found under [/data](/data) as numpy .npy files.

[plot_data_individually.py](plot_data_individually.py)

Creates scatter plots of Tn vs drop number for each valve level for a given set of collected data 

[plot_tn_vs_tnplus1.py](plot_tn_vs_tnplus1.py)

Creates scatter plots comparing Tn vs Tn+1 for each valve level for a gien set of collected data

[plot_3d.py](plot_3d.py)

Creates a 3D scatter plot comparing Tn vs Tn+1 vs Tn+2 for each valve level for a given set of collected data

[plot_all_data_together.py](plot_all_data_together.py)

Plots the drip rates across all valve levels on a single graph.

[generate_images_md.py](generate_images_md.py)

Writes the names of all the images from a certain time-stamped measurement into a .md file for easier export for viewing.

[bifurcation_simulation.py](bifurcation_simulation.py)

Performs simulation of the logistic map equation and generates a bifurcation diagram.

[simulated_data.py](simulated_data.py)

Generates a set of simulated data using the logistic map equation.

# Simulation of Bifurcation Diagram (follow up from prelab)

Using [bifurcation_simulation.py](bifurcation_simulation.py), simulated the logistic equation $x = p x (1-x)$ to create the bifurcation diagram. During the lab, we will try to observe similar relationships from the measurements of the water droplets. 

<img src="bifurcation.png">


# Preliminary Explorations:

Ran [plot_drip_numbers.py](plot_drip_numbers.py) to do an initial pass through all the valve values

Took data for 200 drips at varying valve levels. In order to do a quick sweep, data was collected at valve levels in increments of 20 from 0-100, and increments of 10 from 100-330

<span> <img src="plots/10-13-18-07-46-valve_level=000.png" width=150px></span>
<img src="plots/10-13-18-07-46-valve_level=020.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=040.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=060.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=080.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=100.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=110.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=120.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=130.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=140.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=150.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=160.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=170.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=180.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=190.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=200.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=210.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=220.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=230.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=240.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=250.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=260.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=270.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=280.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=290.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=300.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=310.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=320.png" width=150px>
<img src="plots/10-13-18-07-46-valve_level=330.png" width=150px>

interesting patterns were observed at some of the valve values, namely 180, 270, etc, where the drip rate showed bi-periodic behaviour. However, it was noted that when the data collection was happening, a lot of noise was introduced due the the operation of the pump from the nearby alpha particle experiment, as well as from the movement of people in the lab. These small disturbances created big variations to the data, and so for more stable data collection, will decide to take these measurements overnight, remotely when there is less action inside the lab. 

# Taking more data
Utilizing  [plot_drip_numbers.py](plot_drip_numbers.py), performed data collection overnight. Recorded the drip rates of 1000 drips for valve levels from 340 to 204. The drip rates vs drop number is plotted below for each valve level. 

<span><img src="plots/10-21-02-09-22-valve_level=203.png" width=150px></span>
<img src="plots/10-21-02-09-22-valve_level=204.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=205.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=206.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=207.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=208.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=209.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=210.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=211.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=212.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=213.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=214.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=215.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=216.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=217.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=218.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=219.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=220.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=221.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=222.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=223.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=224.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=225.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=226.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=227.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=228.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=229.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=230.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=231.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=232.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=233.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=234.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=235.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=236.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=237.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=238.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=239.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=240.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=241.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=242.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=243.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=244.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=245.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=246.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=247.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=248.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=249.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=250.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=251.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=252.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=253.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=254.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=255.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=256.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=257.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=258.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=259.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=260.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=261.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=262.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=263.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=264.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=265.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=266.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=267.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=268.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=269.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=270.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=271.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=272.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=273.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=274.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=275.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=276.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=277.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=278.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=279.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=280.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=281.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=282.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=283.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=284.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=285.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=286.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=287.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=288.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=289.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=290.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=291.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=292.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=293.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=294.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=295.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=296.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=297.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=298.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=299.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=300.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=301.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=302.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=303.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=304.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=305.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=306.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=307.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=308.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=309.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=310.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=311.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=312.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=313.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=314.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=315.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=316.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=317.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=318.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=319.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=320.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=321.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=322.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=323.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=324.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=325.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=326.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=327.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=328.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=329.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=330.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=331.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=332.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=333.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=334.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=335.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=336.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=337.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=338.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=339.png" width=150px>
<img src="plots/10-21-02-09-22-valve_level=340.png" width=150px>

# Plotting Tn vs Tn+1

From the same dataset, plotted the drip rate at time N vs the drip rate at time N+1 for all valve levels. 

<span><img src="plots/2d/10-21-02-09-22-valve_level=203.png" width=150px></span>
<img src="plots/2d/10-21-02-09-22-valve_level=204.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=205.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=206.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=207.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=208.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=209.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=210.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=211.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=212.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=213.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=214.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=215.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=216.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=217.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=218.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=219.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=220.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=221.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=222.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=223.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=224.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=225.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=226.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=227.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=228.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=229.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=230.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=231.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=232.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=233.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=234.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=235.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=236.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=237.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=238.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=239.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=240.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=241.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=242.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=243.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=244.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=245.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=246.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=247.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=248.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=249.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=250.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=251.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=252.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=253.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=254.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=255.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=256.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=257.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=258.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=259.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=260.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=261.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=262.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=263.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=264.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=265.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=266.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=267.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=268.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=269.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=270.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=271.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=272.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=273.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=274.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=275.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=276.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=277.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=278.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=279.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=280.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=281.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=282.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=283.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=284.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=285.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=286.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=287.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=288.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=289.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=290.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=291.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=292.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=293.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=294.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=295.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=296.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=297.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=298.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=299.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=300.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=301.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=302.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=303.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=304.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=305.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=306.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=307.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=308.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=309.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=310.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=311.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=312.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=313.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=314.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=315.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=316.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=317.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=318.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=319.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=320.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=321.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=322.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=323.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=324.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=325.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=326.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=327.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=328.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=329.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=330.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=331.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=332.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=333.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=334.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=335.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=336.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=337.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=338.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=339.png" width=150px>
<img src="plots/2d/10-21-02-09-22-valve_level=340.png" width=150px>

# Plotting Tn vs Tn+1 vs Tn+2

Plotted the drip rates at time N vs time N+1 vs time N+2 as a 3D plot.

<span><img src="plots/3d/10-21-02-09-22-valve_level=203.png" width=150px></span>
<img src="plots/3d/10-21-02-09-22-valve_level=204.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=205.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=206.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=207.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=208.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=209.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=210.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=211.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=212.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=213.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=214.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=215.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=216.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=217.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=218.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=219.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=220.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=221.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=222.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=223.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=224.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=225.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=226.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=227.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=228.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=229.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=230.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=231.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=232.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=233.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=234.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=235.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=236.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=237.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=238.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=239.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=240.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=241.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=242.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=243.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=244.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=245.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=246.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=247.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=248.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=249.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=250.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=251.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=252.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=253.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=254.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=255.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=256.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=257.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=258.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=259.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=260.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=261.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=262.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=263.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=264.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=265.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=266.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=267.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=268.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=269.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=270.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=271.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=272.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=273.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=274.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=275.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=276.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=277.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=278.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=279.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=280.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=281.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=282.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=283.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=284.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=285.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=286.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=287.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=288.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=289.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=290.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=291.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=292.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=293.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=294.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=295.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=296.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=297.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=298.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=299.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=300.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=301.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=302.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=303.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=304.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=305.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=306.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=307.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=308.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=309.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=310.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=311.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=312.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=313.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=314.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=315.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=316.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=317.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=318.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=319.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=320.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=321.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=322.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=323.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=324.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=325.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=326.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=327.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=328.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=329.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=330.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=331.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=332.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=333.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=334.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=335.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=336.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=337.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=338.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=339.png" width=150px>
<img src="plots/3d/10-21-02-09-22-valve_level=340.png" width=150px>


# Generating Bifurcation Diagram

Plotted the drip rates across all valve levels in a continuos array.

<img src="plots/bifurcation/10-21-02-09-22-data-bifurcation.png">

Plotted the drip rates across all valve levels as a scatter plot of the last 50 Tn's on the y-axis vs the valve level on the x-axis

<img src="plots/bifurcation/10-21-02-09-22-point-data.png">

### We observe that there are obvious regions of bifurcation in the plot, and the time between success drips follow a decreasing trend as the valve level increases. 

# Collecting data for longer time-frames

Repeated the data collection process, this time with 5000 points at each level. Due to time constraints, only levels 295 - 340 were collected.

<span><img src="plots/10-28-01-07-45-valve_level=295.png" width=150px></span>
<img src="plots/10-28-01-07-45-valve_level=296.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=297.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=298.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=299.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=300.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=301.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=302.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=303.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=304.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=305.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=306.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=307.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=308.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=309.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=310.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=311.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=312.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=313.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=314.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=315.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=316.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=317.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=318.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=319.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=320.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=321.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=322.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=323.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=324.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=325.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=326.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=327.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=328.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=329.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=330.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=331.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=332.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=333.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=334.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=335.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=336.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=337.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=338.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=339.png" width=150px>
<img src="plots/10-28-01-07-45-valve_level=340.png" width=150px>


# Now plotting Tn vs Tn+1
<span><img src="plots/2d/10-28-01-07-45-valve_level=295.png" width=150px></span>
<img src="plots/2d/10-28-01-07-45-valve_level=296.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=297.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=298.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=299.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=300.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=301.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=302.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=303.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=304.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=305.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=306.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=307.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=308.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=309.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=310.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=311.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=312.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=313.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=314.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=315.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=316.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=317.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=318.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=319.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=320.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=321.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=322.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=323.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=324.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=325.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=326.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=327.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=328.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=329.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=330.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=331.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=332.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=333.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=334.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=335.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=336.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=337.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=338.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=339.png" width=150px>
<img src="plots/2d/10-28-01-07-45-valve_level=340.png" width=150px>


# Now plotting in Tn vs Tn+1 vs Tn+2
<span><img src="plots/3d/10-28-01-07-45-valve_level=295.png" width=150px></span>
<img src="plots/3d/10-28-01-07-45-valve_level=296.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=297.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=298.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=299.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=300.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=301.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=302.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=303.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=304.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=305.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=306.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=307.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=308.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=309.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=310.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=311.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=312.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=313.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=314.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=315.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=316.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=317.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=318.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=319.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=320.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=321.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=322.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=323.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=324.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=325.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=326.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=327.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=328.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=329.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=330.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=331.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=332.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=333.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=334.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=335.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=336.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=337.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=338.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=339.png" width=150px>
<img src="plots/3d/10-28-01-07-45-valve_level=340.png" width=150px>

# Bifurcation diagram with all the data

Plotted the drip rates across all valve levels as a continuous array. 

<img src="plots/bifurcation/10-28-01-07-45-data-bifurcation.png">

Plotted the drip rates across all valve levels as a scatter plot of the last 100 Tn's on the y-axis vs the valve level on the x-axis

<img src="plots/bifurcation/10-28-01-07-45-point-data.png">

### We note that even though 5000 drops were taken for each level, there appear to be more noise in the data. This may have been due to the fact that there was a conflict in measurements and another student was also performing data collection on the experiment during the same time. There may have also been additional perturbations in the lab during the data collection time (ie the pump may have been turned on for some period of the data collection)

### For the following analysis, we will look at data collected from both experiments (5000pts and 1000pts) 

# Analysis

As proposed in the paper "Chaotic Rhythms of a Dripping Faucet" (Robert F. Cahalan, Henning Leidecker and Gabriel D. Cahalan), many trends can be seen from the data. 

## Trends in drip rate (Cahalan et al.), Figure 4.

<img src="plots/from_paper/Fig4.jpg" width="500px">

### Similar trends can be observed from our data. For example:

|  |  |
| :---: | :---: |
| Drift can be observed at a valve level of 221 (1k pts)| Missing drops can be observed at a valve level of 208 (1k pts) |
| <img src="plots/10-21-02-09-22-valve_level=221.png" width="300px"> | <img src="plots/10-21-02-09-22-valve_level=208.png" width="300px"> |
| | |
| Random Scatter can be observed at a valve level of 239 (1k pts) | Non-stationarity  can be observed at a valve level of 300 (5k pts)|
| <img src="plots/10-21-02-09-22-valve_level=239.png" width="300px"> | <img src="plots/10-28-01-07-45-valve_level=300.png" width="300px"> |


## Trends in Lower Drip rates

Based on Figure 5 (Cahalan et al.), as drip rate increase, we begin to observe the onset of chaos

<img src="plots/from_paper/Fig5.jpg" width="500px">

|  |  |
| :---: | :---: |
| Periodic case can be observed at a valve level 228 (1k pts) | Biperiodic case can be observed at a valve level of 256 (1k pts)|
| <img src="plots/10-21-02-09-22-valve_level=228.png" width="300px"> | <img src="plots/10-21-02-09-22-valve_level=256.png" width="300px"> |
| | |
| Chaos can be observed at a valve level of 295 (1k pts) | Another case of chaos  can be observed at a valve level of 314 (5k pts) |
| <img src="plots/10-21-02-09-22-valve_level=295.png" width="300px"> | <img src="plots/10-28-01-07-45-valve_level=314.png" width="300px"> |


## Trends in Successive drip rates 

From Figure 6 (Cahalan et al.), the following trends were observed when plotting Tn vs Tn+1

<img src="plots/from_paper/Fig6.jpg" width="500px">

Using the cases that we observed, these trends are also plotted

|  |  |
| :---: | :---: |
| Periodic dripping can be observed at a valve level 228 (1k pts) | Biperiodic dripping can be observed at a valve level of 256 (1k pts)|
| <img src="plots/2d/10-21-02-09-22-valve_level=228.png" width="300px"> | <img src="plots/2d/10-21-02-09-22-valve_level=256.png" width="300px"> |
| | |
| "Parabola" can be observed at a valve level of 295 (1k pts) | "Camel"  can be observed at a valve level of 314 (5k pts) |
| <img src="plots/2d/10-21-02-09-22-valve_level=295.png" width="300px"> | <img src="plots/2d/10-28-01-07-45-valve_level=314.png" width="300px"> |

We note that at level 295, the Tn vs drip number plot is not a perfect match for the figure shown in the paper. The upside-down parabola with valve level 318 (see more analysis below) better matches the Tn vs Tn+1 and 3D plots. 

## The Henon Attractor
Based on figure 7 from Cahlana et al., the Henon attractor is observed when plotting Tn vs Tn+1 vs Tn+2 in a 3D plot, for the "parabola" case seen in the 2D plot. 

<img src="plots/from_paper/Fig7.jpg" width="500px">

For level = 295, we observe the following Henon attractor in 3D.

<img src="plots/3d/10-21-02-09-22-valve_level=295.png" width="300px">

A more closely matched pattern can be observed when we look at the case for valve level = 318, apart from the difference that in the 2D case the "parabola" is flipped upside down as from the paper. However, plots of Tn vs drip number and the 3D Henon attractor is very similar to the figure described in the paper. 

<span><img src="plots/10-21-02-09-22-valve_level=318.png" width="300px"></span>
<span><img src="plots/2d/10-21-02-09-22-valve_level=318.png" width="300px"></span>
<span><img src="plots/3d/10-21-02-09-22-valve_level=318.png" width="300px"></span>

# More interesting cases

Using both set of our data, we search for the patterns as depicted in Figure 8 and 9 from the paper. 

<img src="plots/from_paper/Fig8.jpg">

## Cobra: 
valve level = 314

<span><img src="plots/10-28-01-07-45-valve_level=314.png" width="300px"></span>
<span><img src="plots/2d/10-28-01-07-45-valve_level=314.png" width="300px"></span>
<span><img src="plots/3d/10-28-01-07-45-valve_level=314.png" width="300px"></span>


## Adders
valve level = 311

<span><img src="plots/10-28-01-07-45-valve_level=311.png" width="300px"></span>
<span><img src="plots/2d/10-28-01-07-45-valve_level=311.png" width="300px"></span>
<span><img src="plots/3d/10-28-01-07-45-valve_level=311.png" width="300px"></span>

## Ring
large scale pattern is seen at valve level 269, but when zoomed in, the ring is not observed

<span><img src="plots/10-21-02-09-22-valve_level=269.png" width="300px"></span>
<span><img src="plots/2d/10-21-02-09-22-valve_level=269.png" width="300px"></span>
<span><img src="plots/3d/10-21-02-09-22-valve_level=269.png" width="300px"></span>

zoomed:

<span><img src="plots/specific/10-21-02-09-22-valve_level=269.png" width="300px"></span>

## Ostritch

<span><img src="plots/10-28-01-07-45-valve_level=319.png" width="300px"></span>
<span><img src="plots/2d/10-28-01-07-45-valve_level=319.png" width="300px"></span>
<span><img src="plots/3d/10-28-01-07-45-valve_level=319.png" width="300px"></span>

## Dispersed groups

<span><img src="plots/10-28-01-07-45-valve_level=331.png" width="300px"></span>
<span><img src="plots/2d/10-28-01-07-45-valve_level=331.png" width="300px"></span>
<span><img src="plots/3d/10-28-01-07-45-valve_level=331.png" width="300px"></span>


## Sphinx

<span><img src="plots/10-28-01-07-45-valve_level=334.png" width="300px"></span>
<span><img src="plots/2d/10-28-01-07-45-valve_level=334.png" width="300px"></span>
<span><img src="plots/3d/10-28-01-07-45-valve_level=334.png" width="300px"></span>


# Long term trend of valve level 306

From the data collected at 5k points for valve level 306 revealed some very interesting trends
### Tn vs drop number 

<span><img src="plots/10-28-01-07-45-valve_level=306.png" width="300px"></span>

### Tn vs Tn+1

<span><img src="plots/2d/10-28-01-07-45-valve_level=306.png" width="300px"></span>

### Tn vs Tn+1 vs Tn+2

<span><img src="plots/3d/10-28-01-07-45-valve_level=306.png" width="300px"></span>

Finding the following trend particularly interesting, we investigate the long term behaviour of drip rates at a valve level of 306. Data was recorded at this level for around 240000 drops.

### Tn vs Drop Number

<span><img src="plots/10-29-01-46-32-valve_level=306.png" width="300px"></span>

### Tn vs Tn+1

<span><img src="plots/2d/10-29-01-46-32-valve_level=306.png" width="300px"></span>

### Tn vs Tn+1 vs Tn+2

<span><img src="plots/3d/10-29-01-46-32-valve_level=306.png" width="300px"></span>

Interestingly, the "ring" pattern from paper shown before appears in the graph of Tn vs Tn+1

# Simulated Data

using [simulated_data.py](simulated_data.py), performed the same analysis but utilizing a dataset of "simulated" drops generated from the logistic map equation. Each "valve-level" corresponds a value of 200p.
We ignore the cases for p < 687 as they are not very interesting.

## Tn vs Drop number (simulations)

<span><img src="plots/00-00-00-00-00-valve_level=687.png" width=150px></span>
<img src="plots/00-00-00-00-00-valve_level=688.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=689.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=690.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=691.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=692.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=693.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=694.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=695.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=696.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=697.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=698.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=699.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=700.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=701.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=702.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=703.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=704.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=705.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=706.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=707.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=708.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=709.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=710.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=711.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=712.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=713.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=714.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=715.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=716.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=717.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=718.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=719.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=720.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=721.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=722.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=723.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=724.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=725.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=726.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=727.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=728.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=729.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=730.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=731.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=732.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=733.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=734.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=735.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=736.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=737.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=738.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=739.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=740.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=741.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=742.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=743.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=744.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=745.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=746.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=747.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=748.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=749.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=750.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=751.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=752.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=753.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=754.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=755.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=756.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=757.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=758.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=759.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=760.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=761.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=762.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=763.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=764.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=765.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=766.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=767.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=768.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=769.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=770.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=771.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=772.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=773.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=774.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=775.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=776.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=777.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=778.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=779.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=780.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=781.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=782.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=783.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=784.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=785.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=786.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=787.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=788.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=789.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=790.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=791.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=792.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=793.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=794.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=795.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=796.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=797.png" width=150px>
<img src="plots/00-00-00-00-00-valve_level=798.png" width=150px>

## Tn vs Tn+1

<span><img src="plots/2d/00-00-00-00-00-valve_level=687.png" width=150px><span>
<img src="plots/2d/00-00-00-00-00-valve_level=688.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=689.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=690.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=691.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=692.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=693.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=694.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=695.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=696.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=697.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=698.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=699.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=700.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=701.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=702.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=703.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=704.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=705.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=706.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=707.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=708.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=709.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=710.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=711.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=712.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=713.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=714.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=715.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=716.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=717.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=718.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=719.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=720.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=721.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=722.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=723.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=724.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=725.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=726.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=727.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=728.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=729.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=730.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=731.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=732.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=733.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=734.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=735.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=736.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=737.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=738.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=739.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=740.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=741.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=742.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=743.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=744.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=745.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=746.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=747.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=748.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=749.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=750.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=751.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=752.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=753.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=754.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=755.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=756.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=757.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=758.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=759.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=760.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=761.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=762.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=763.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=764.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=765.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=766.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=767.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=768.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=769.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=770.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=771.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=772.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=773.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=774.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=775.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=776.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=777.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=778.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=779.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=780.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=781.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=782.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=783.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=784.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=785.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=786.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=787.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=788.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=789.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=790.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=791.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=792.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=793.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=794.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=795.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=796.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=797.png" width=150px>
<img src="plots/2d/00-00-00-00-00-valve_level=798.png" width=150px>

# Tn vs Tn+2 vs Tn+2 

<span><img src="plots/3d/00-00-00-00-00-valve_level=687.png" width=150px></span>
<img src="plots/3d/00-00-00-00-00-valve_level=688.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=689.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=690.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=691.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=692.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=693.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=694.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=695.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=696.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=697.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=698.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=699.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=700.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=701.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=702.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=703.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=704.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=705.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=706.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=707.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=708.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=709.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=710.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=711.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=712.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=713.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=714.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=715.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=716.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=717.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=718.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=719.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=720.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=721.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=722.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=723.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=724.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=725.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=726.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=727.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=728.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=729.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=730.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=731.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=732.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=733.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=734.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=735.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=736.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=737.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=738.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=739.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=740.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=741.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=742.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=743.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=744.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=745.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=746.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=747.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=748.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=749.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=750.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=751.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=752.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=753.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=754.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=755.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=756.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=757.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=758.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=759.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=760.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=761.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=762.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=763.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=764.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=765.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=766.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=767.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=768.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=769.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=770.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=771.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=772.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=773.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=774.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=775.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=776.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=777.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=778.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=779.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=780.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=781.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=782.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=783.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=784.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=785.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=786.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=787.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=788.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=789.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=790.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=791.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=792.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=793.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=794.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=795.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=796.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=797.png" width=150px>
<img src="plots/3d/00-00-00-00-00-valve_level=798.png" width=150px>

## We note that the behaviour simulated by the logistic map is not very interesting. We do see the case of Tn vs Tn+1 showing in the parabolic case, as well as non-stationary cases. We also observe the ideal Henon attractor when the plots are made in 3D.

# Conclusions

In this experiment, we measured the drip rates of a "leaky tap" using a photoemitter-detector pair. We explored the trends in the drip rate as the valve level of the apparatus was changed. Above a drip rate, we observed that the time between drips exhibited chaotic behviour as well as a wide range of other behaviours. Following the trends observed in the paper "Chaotic Rhythms of a Dripping Faucet" (Robert F. Cahalan, Henning Leidecker and Gabriel D. Cahalan), we analyzed our data and observed similar trends to the ones observed in the paper. Through the data we collected, we were able to reproduce most of the cases outlined in the paper. Specifically, we plotted the drip rate vs drop number in a 1-dimensional plot, drip rate vs succesive drip rate (Tn vs Tn+1) in a 2-dimensional plot, and Tn vs Tn+1 vs Tn+2 in a 3-dimensional plot. Many interesting chaotic trends were observed for various levels. The trend of drip rates across all valve level was also made and the corresponding behvaiour of points when the system enters into chaos can be observed. 

We also simulated data using the logistic map equation, and reproduced an ideal "parabolic" behaviour of the Tn vs Tn+1 plot as well as the ideal Henon attractor in 3D. 

Further analyses could be made on some of these measurements, such as retaking data at each level to observe if such results are reproducilbe across multiple session. One can suspect that the water level in the tank could also be an influence to the behviours of the drips, and this could be something to be considered as well. Further analysis such as the one performed at valve-level=306 can be done for other levels as well and to see what the behaviour is at those levels. 

Due to the noise experienced inside the lab environment, particularly due to the usage of the pump for other experiment, it was difficult to collect high quality data. For future data collection, it would be recommeneded to collect overnight or during hours when there are less disturbances in the laboratory environment. Another blocker was due to the required speed for data collection, as waiting for data was quite time consuming. Given more time, we beleive that more detailed analysis could be done on the data. 


