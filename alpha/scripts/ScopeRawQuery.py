#!/usr/bin/env python3

from xml.sax import default_parser_list
import numpy as np
import sys
import pyvisa as visa
from matplotlib import pyplot as plt
import argparse
import time

# sys.exit('This code is provided as a start.  Copy to your workspace and edit it')

# Based on examples in e.g.
# https://gist.github.com/prhuft/8d961e2983bfdf8fdf1effcc1aae61a9
# https://gist.github.com/pklaus/7e4cbac1009b668eafab
# https://www.codeproject.com/Articles/869421/Interfacing-Rigol-Oscilloscopes-with-C 

# Programming guide for this oscilloscope:
# https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-af444326-0551-4fd5-a277-bf8fff6f53cb/1/-/-/-/-/DS1000Z-E_ProgrammingGuide_EN.pdf


def getScopeTraceRaw(triggerLevel : float = None, triggerChannel: str = None, readChannel:str = None):
    # Since we can only collect a bit of data at a time on these scopes,
    # walk through the size of the trace samples and accumulate them here.
    def get_data(scope,mdepth) :
        print("About to fetch data in {0} points...".format(mdepth))
        fulldata = []
        points_list = list(range(489, mdepth, 489))
        points_list.append(mdepth)
        for thisindex, endpoint in enumerate(points_list) :
            if thisindex != 0 :
                startpoint = points_list[thisindex-1]+1
            else :
                startpoint = 1
            scope.write(":WAV:STAR {0}".format(startpoint))
            scope.write(":WAV:STOP {0}".format(endpoint)) # 489 is the maximum distance between start and end
            try :
                rawdata = scope.query_binary_values(':WAV:DATA?', datatype = 'I', container = np.array)
            except :
                # fill it with zeros
                print("Data collection failed for points",startpoint,endpoint)
                rawdata=np.array([])
                print("raw data is",rawdata)
            fulldata = np.append(fulldata,rawdata)
            # NOTE: 
            # After retrieving data, you will get a crash if you
            # attempt to check :WAV:STOP. It is fine before, but
            # broken after. You can still set it but you can't read it.
        normalised_data = fulldata

        return normalised_data
    

    # Make the pyvisa resource manager
    rm = visa.ResourceManager()
    # Get the USB device, e.g. 'USB0::0x1AB1::0x0588::DS1ED141904883'
    instruments = rm.list_resources()
    usbs = list(filter(lambda x: 'USB' in x, instruments))
    scope_address = ""
    for address in usbs :
        if "::DS" in address :
            scope_address = address
    if not scope_address :
        print("Could not find address of scope!")
        exit(1)

    print("Will open instrument",scope_address)

    scope = rm.open_resource(scope_address, timeout=2000, chunk_size=1024000)

    # Ensure scope running
    scope.write(":RUN")

    # Set trigger channel
    if (triggerChannel) :
        print("You requested to set the trigger channel to",triggerChannel)
        scope.write(":TRIG:EDG:SOUR {0}".format(triggerChannel)) 
        print("Source is now",scope.query(":TRIG:EDG:SOUR?"))

    # Sets trigger level.
    if (triggerLevel) :
        scope.write(":TRIG:EDG:LEV {0}".format(triggerLevel))

    # Wait a second to make sure we trigger
    time.sleep(1)


    # Check the sample rate
    sample_rate = scope.query(':ACQ:SRAT?')
    timescale = float(scope.query(":TIM:SCAL?"))

    # Note: not :WAV:POIN:MODE, which is for other DS1000-series Rigol scopes
    # Byte return format is a value between 0 and 255

    #  Important:  The scope has different commands for which channel to get a trace from
    #                                               and which channel to measure from !!
    #______________________

    scope.write(":WAV:SOUR {0}".format(readChannel))
    scope.write(":MEAS:SOUR {0}".format(readChannel))

    # Try for now, at least
    scope.write(":ACQ:MDEP 6000")

    # Get the trace
    mdepth = int(float(sample_rate)*timescale*12.) # This is the true mdepth, regardless of what we set
    dataset=np.array([])
    for k in range(10):
        scope.write(":STOP")

        v = float(scope.query(":MEAS:VMAX?"))

        dataset=np.append(dataset, v)

        scope.write(":RUN")
        time.sleep(.4)

    # Turn back on
    scope.write(":RUN")

    # Release scope for next call
    rm.close()
    scope.close()

    # If requested, format and save everything to an output file
    #save all of our voltages that were stored in myArray

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%m-%d-%H-%M-%S")

    if not os.path.exists('data'):
        os.makedirs('data')
    fname1 = 'data/{0}-Voltages.dat'.format(dt_string)
    np.savetxt(fname1, default_parser_list, delimiter=",")
    print('saved to',fname1)
    #save the time axis array as well. We'll need this
    fname2 = 'data/{0}-Times.dat'.format(dt_string)
    np.savetxt(fname2, time_axis, delimiter=",")
    print('saved to',fname2)

    times = np.genfromtxt(fname1)
    voltages = np.genfromtxt(fname2)
    return times, voltages



