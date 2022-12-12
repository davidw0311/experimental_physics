import numpy as np

times = np.load("data/vvolt_vs_time_times.npy")
vvolts = np.load("data/vvolt_vs_time_vvolts.npy")

def getRoomvalveTime(v_start, v_end):
    
    # find the index of the voltage that is closest to v_start but higher in array
    # with help from https://stackoverflow.com/questions/55769522/how-to-find-maximum-negative-and-minimum-positive-number-in-a-numpy-array
    high_index = np.where(vvolts-v_start > 0, vvolts-v_start, np.inf).argmin()
    low_index = high_index + 1
    
    # check indices are not out of bounds
    
    t0 = (vvolts[high_index] - v_start)/(vvolts[high_index] - vvolts[low_index]) + times[high_index]
    
    high_index = np.where(vvolts-v_end > 0, vvolts-v_end, np.inf).argmin()
    low_index = high_index + 1
    tf = (vvolts[high_index] - v_end)/(vvolts[high_index] - vvolts[low_index]) + times[high_index]
    
    dt = tf-t0
    
    return dt