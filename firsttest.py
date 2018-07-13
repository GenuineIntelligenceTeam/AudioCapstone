#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:44:15 2018

@author: caseygoldstein
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure
from microphone import record_audio


###########################

def micToDAS(listen_time):
    """ Parameters
        ----------
        listen_time : the time in seconds that microphone records
        Returns
        ----------
        audio_data : a numpy array that contains the digitized audio data"""

    byte_encoded_signal, sampling_rate = record_audio(listen_time)
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in byte_encoded_signal])
    return audio_data

###########################

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


###########################
FOOTPRINT_BASIC = generate_binary_structure(rank=2, connectivity=1)   
def generate_fingerprint(spectrogram, fp=FOOTPRINT_BASIC, cutoff=0.0, fanout=30):
    peak_times, peak_frequencies = find_peaks(spectrogram, fp, cutoff)

    N_peaks = len(peak_times)

    fingerprint = []
    for n in range(N_peaks-1):
        for j in range(n + 1, n +1 + fanout):
            try:
                fingerprint.append((peak_frequencies[n], peak_frequencies[j], peak_times[j] - peak_times[n]))
            except IndexError:
                print('n: ' + str(n))
                print('j: ' + str(j))

    return fingerprint    


###########################

def find_peaks(spectrogram, fp=FOOTPRINT_BASIC, cutoff=0.0):
    filtered_spectrogram = maximum_filter(spectrogram, footprint=fp)

    spectrogram_peaks = (spectrogram == filtered_spectrogram)
    spectrogram_peaks *= (spectrogram >= cutoff)

    time, freq = np.where(spectrogram_peaks)
    return time, freq

###########################

def DigToSpec(audioData):
    return mlab.specgram(audioData, NFFT=4096, Fs=44100,window=mlab.window_hanning,noverlap=4096 // 2)
    
###########################  
    
 
    
with open("/Users/caseygoldstein/Desktop/trumpet_copy.txt", 'r') as R:
    trumpet_audio = np.asarray([int(i.split("\n")[0]) for i in R if i.split("\n")[0] is not ''])


testspec = DigToSpec(trumpet_audio)
testspec = testspec[0]
threshold = findthreshold(testspec)



OurFirstFingerprint = generate_fingerprint(testspec,fp=FOOTPRINT_BASIC,cutoff=threshold,fanout=30)

