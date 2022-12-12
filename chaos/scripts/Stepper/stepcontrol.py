#!/usr/bin/env python3 
import configparser
import time
import fcntl
import os
import sys
import StepClass
  
def controlStepper(name="David", motor=2, step=1, stepspersec=1):
    #28BYJ-48 (at least our version) has 2048 steps per rev, with /4 microstep = 8192
    #with default stepmultplier 16 this becomes 512 steps/rev
    #======

    N=open('/home/student/Stepper/users','a')
    import datetime
    dto=datetime.datetime.now()
    # S=input('what is your name?')

    N.write(name+'  '+str(dto)+'\n')
    N.close()


    #=========



    #Create and open a temporary file to prevent multiple instances of script
    lock_file_pointer = os.open(f"/home/public/instance_stepper.lock", os.O_WRONLY | os.O_CREAT)
    fcntl.lockf(lock_file_pointer, fcntl.LOCK_EX | fcntl.LOCK_NB)

    config = configparser.ConfigParser()
    config.read('/home/public/stepconfig.ini')

    # Turn on Power.  Harmless if it is already on.
    os.system('curl http://smartplug1/cm?cmnd=Power+On')
    print('Power ON')

    #Read number of motors from config
    nummotors = int(config['GENERAL']['NumMotors'])
    print("Using " + str(nummotors) + " motors")

    motorlist = []

    for i in range(nummotors):
        print("Motor " + str(i+1) + " alias: " + config['MOTOR' + str(i+1)]['Alias'])
        motorlist.append(StepClass.twostep(confname = ('MOTOR' + str(i+1))))
    print(" But please remember, camera may be rotated!")
        
    print("Starting Locations:  ", end = '')
    for i in range(nummotors):
        if i < nummotors -1:
            print(str(motorlist[i].mpos) + ',',  end = '')
        else:
            print(str(motorlist[i].mpos))

    print('  ')

    #print('Going to default positions')
    #for i in range(nummotors):
    #    print("Current motor " + str(i+1) + " position: " + config['MOTOR' + str(i+1)]['CurrentSteps'], end='')
    #    print("   Moving to  " + config['MOTOR' + str(i+1)]['DefaultSteps'])
    #    motorlist[i].move(int(config['MOTOR' + str(i+1)]['DefaultSteps']) - int(config['MOTOR' + str(i+1)]['CurrentSteps']), int(config['MOTOR' + str(i+1)]['MaxSpeed']))

    #print('    ')    
    #print("New Locations:  ", end= '')    
    #for i in range(nummotors):
    #    if i < nummotors -1:
    #        print(str(motorlist[i].mpos) + ',',  end = '')
    #    else:
    #        print(str(motorlist[i].mpos))


        
    #default command
    #command = "1,1,1"
    #commandlist = command.split(",")

    print( 'Motion commands are (motor numb), (+- N Steps), (steps/second). <cr> to repeat, q to quit' )

    run = 1
    commandlist = [motor, step, stepspersec]
                        
    motornumber = int(commandlist[0])
    if(motornumber > 0 and motornumber <= nummotors):
        motorlist[motornumber - 1].move(int(commandlist[1]), int(commandlist[2]))
        #print("New motor " + str(motornumber) + " position: " + str(motorlist[motornumber - 1].mpos))
    
    print("Current Locations:  ", end = '')
    for i in range(nummotors):
        if i < nummotors -1:
            print(str(motorlist[i].mpos) + ',',  end = '')
        else:
            print(str(motorlist[i].mpos), end ='')        

        
    print('Ending.')
    print('Ending.  Remember the power switch!!')
    print('I bet you will forget.  I will get it.')
    os.system('curl http://smartplug1/cm?cmnd=Power+Off')
    print('')
    

