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


def getVoltage(triggerLevel : float = None, triggerChannel: str = None, readChannel:str = None):
 
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

    # print("Will open instrument",scope_address)

    scope = rm.open_resource(scope_address, timeout=2000, chunk_size=1024000)

    vmin = float(scope.query(":MEAS:VMIN?").strip())
    vmax = float(scope.query(":MEAS:VMAX?"))
        
    # Release scope for next call
    rm.close()
    scope.close()


    return vmin, vmax

import time 
if __name__ == "__main__":
    for i in range(5):
        print(getVoltage())


