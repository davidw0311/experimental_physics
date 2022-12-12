#!/usr/bin/env python3

import pigpio
import time

def countTriggers(duration):
   print(f'counting number of triggers in {duration} seconds')
   GATE1=5

   global trigger_count
   trigger_count = 0

   def cbf(gpio, level, tick):
      if level==0:
         trigger_time = tick
         global trigger_count
         trigger_count += 1


   pi = pigpio.pi() # Connect to local Pi.
   cb1 = pi.callback(GATE1, pigpio.EITHER_EDGE, cbf)

   start_time = time.time()
   current_time = time.time() - start_time

   while True:
      if current_time < duration:
         current_time = time.time() - start_time
      else:
         break
      
   cb1.cancel()
   pi.stop()
   
   return trigger_count
