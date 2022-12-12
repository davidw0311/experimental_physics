#!/usr/bin/env python3 
import os
import sys
import configparser
import time
import fcntl
import datetime
import click
import StepClass

#28BYJ-48 (at least our version) has 2048 steps per rev, with /4 microstep = 8192
#with default stepmultplier 16 this becomes 512 steps/rev
#======

@click.command()
@click.option('-r','--release', default=False, is_flag=True,
              help='release the lock when you are done with programmatic stepper motor access')
@click.argument('name', nargs=1)
@click.argument('command', nargs=-1)
def controlMotor(name, command, release):
    '''Control Stepper motor through command-line interface. 
    Invocation needs to provide NAME of caller and 
    COMMAND (a string containing 3 numbers separated by commas or space)

    A typical session starts with the invocation with NAME and COMMAND and will be successful as
    long as nobody holds the lock. Subsequent invocation with the same NAME will be successful.
    At the end, user should invoke program with flag -r (--release) and the username to free
    access for other users.
    '''
    fname_config = '/home/public/stepconfig.ini'
    dto=datetime.datetime.now()
    
    #Create and open a temporary file to prevent multiple instances of script
    lock_file_pointer = os.open(f"/home/public/instance_stepper.lock", os.O_WRONLY | os.O_CREAT)
    fcntl.lockf(lock_file_pointer, fcntl.LOCK_EX | fcntl.LOCK_NB)
    # Also create a mutex (inside the config file)
    # so that other processes are aware that we are using the stepper motor
    config = configparser.ConfigParser()
    config.read(fname_config)

    if release:
        if config['GENERAL']['InUseBy']=="" and config['GENERAL']['InUseWhen']=="":
            print('mutex already released?')
            sys.exit(0)
        else:
            if name == config['GENERAL']['InUseBy']:
                config['GENERAL']['InUseBy']=""
                config['GENERAL']['InUseWhen']=""
                with open(fname_config, 'w') as conf:
                    config.write(conf)
                print('mutex released')
                sys.exit(0)
            else:
                print('Can not release mutex held by other user (did you mistype your name?)')
                sys.exit(126)
    if name == config['GENERAL']['InUseBy']:
         print('mutex OK; proceeding...')
    elif config['GENERAL']['InUseBy']=="" and config['GENERAL']['InUseWhen']=="":
         config['GENERAL']['InUseBy']=name
         config['GENERAL']['InUseWhen']='{}'.format(dto)
         with open(fname_config, 'w') as conf:
             config.write(conf)
         print('mutex created')
    else:
         print('mutex held by other user (did you mistype your name?)')
         sys.exit(126)
    
    with open('/home/student/Stepper/users','a') as logfile:
        logfile.write(name+'  '+str(dto)+'\n')

    # Turn on Power.  Harmless if it is already on.
    os.system('curl http://smartplug1/cm?cmnd=Power+On')
    
    # Motion commands are (motor numb), (+- N Steps), (steps/second)
    #command = "1,1,1"
    if len(command) == 0:
        print('need command unless only lock is released')
        sys.exit(1)
    elif len(command) == 1: #no spaces around the commas..
        commandlist = command[0].split(",")
    else:
        commandlist = [c.strip(',') for c in command]
    print('command to be issued: ',commandlist)
    #sys.exit(0)

    #Read number of motors from config
    nummotors = int(config['GENERAL']['NumMotors'])
    motorlist = []
    
    for i in range(nummotors):
        print("Motor " + str(i+1) + " alias: " + config['MOTOR' + str(i+1)]['Alias'])
        motorlist.append(StepClass.twostep(confname = ('MOTOR' + str(i+1))))
            
    motornumber = int(commandlist[0])
    if(motornumber > 0 and motornumber <= nummotors):
        motorlist[motornumber - 1].move(int(commandlist[1]), int(commandlist[2]))
    
    print("Current Locations:  ", end = '')
    for i in range(nummotors):
        if i < nummotors -1:
            print(str(motorlist[i].mpos) + ',',  end = '')
        else:
            print(str(motorlist[i].mpos), end ='')        

    # Remember the power switch!
    os.system('curl http://smartplug1/cm?cmnd=Power+Off')

if __name__ == '__main__':
    controlMotor();
