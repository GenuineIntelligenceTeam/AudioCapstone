#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:20:58 2018

@author: caseygoldstein
"""

#creates histogram - 
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure
def findthreshold (specArray):
    flattenedArray = specArray.flatten()
    absArray = np.abs(flattenedArray)
    loggedArray = np.log(absArray)
    print(loggedArray.shape)
    
    
    hist,bins = np.histogram(loggedArray,len(loggedArray)//2,density = True)
    cumulative_distr = np.zeros(len(hist))
    binsize = np.diff(bins)
    cumulative_distr = (np.cumsum(hist*binsize))
    
    print('hist:' + str(len(hist)))
    bin_index_of_cutoff = np.searchsorted(cumulative_distr, 0.9)
    cutoff_log_amplitude = bins[bin_index_of_cutoff]
    return cutoff_log_amplitude


with open("/Users/caseygoldstein/Desktop/trumpet_copy.txt", 'r') as R:
    trumpet_audio = np.asarray([int(i.split("\n")[0]) for i in R if i.split("\n")[0] is not ''])
    

sampling_rate = 44100 # sampling rate in Hz

fig, ax = plt.subplots()
S, freqs, times, im = ax.specgram(trumpet_audio, NFFT=4096, Fs=sampling_rate,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)

print('return:' + str(findthreshold(S)))


    
