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

"""
Inputs: specArray (shape M,N) -  spectrogram data in 2D array
Outputs: cutoff_log_amplitude - Threshold value between foreground/background of spectrogram
"""





def findthreshold (specArray):
    flattenedArray = specArray.flatten()
    absArray = np.abs(flattenedArray)
    loggedArray = np.log(absArray)
    return np.percentile(loggedArray,90)
    
with open("/Users/caseygoldstein/Week1_Student/Day2/data/trumpet.txt", 'r') as R:
    trumpet_audio = np.asarray([int(i) for i in R])
    
<<<<<<< HEAD
sampling_rate = 44100 # sampling rate in Hz

fig,ax = plt.subplots()
S, freqs, times, im = ax.specgram(trumpet_audio, NFFT=4096, Fs=sampling_rate,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)

print(newfindthreshold(S))


=======
    hist,bins = np.histogram(loggedArray,len(loggedArray)//2,density = True)
    cumulative_distr = np.zeros(len(hist))
    binsize = np.diff(bins)
    cumulative_distr = (np.cumsum(hist*binsize))
    
    print('hist:' + str(len(hist)))
    bin_index_of_cutoff = np.searchsorted(cumulative_distr, 0.9)
    cutoff_log_amplitude = bins[bin_index_of_cutoff]
    return cutoff_log_amplitude
>>>>>>> d35075012f786b09ec621fa562c0cd67ca307b5a
