#!/usr/bin/env python3

import pigpio
import time
from tqdm import tqdm


def getDroprates(count_array_length=100):
    print(f'-----------------counting {count_array_length} drops!-----------------')
    pbar = tqdm(total=count_array_length)
    
    GATE1=26

    global counts 
    counts = []
    
    global last_tick 
    last_tick = None
    def cbf(gpio, level, tick):
        global last_tick, counts
        if level==0:
            if last_tick is None:
                last_tick = tick
            else:
                counts.append(tick-last_tick)
                last_tick = tick
                pbar.update(1)

    pi = pigpio.pi() # Connect to local Pi.
    cb1 = pi.callback(GATE1, pigpio.EITHER_EDGE, cbf)
    
    while len(counts) < count_array_length:
        pass

    
    cb1.cancel()
    pi.stop()
    
    return counts
