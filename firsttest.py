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
import librosa
 




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
    print('did this')
    absArray = np.abs(flattenedArray)
    print('did that')
    absArray +=0.0000000000000000000000000000000001
    loggedArray = np.log(absArray)
    print(loggedArray.shape)
    
    
    hist,bins = np.histogram(loggedArray,bins = len(loggedArray)//2, range = (loggedArray.min(),loggedArray.max()),density = True)
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
    for n in range(N_peaks):
        for j in range(n + 1, min(n + 1 + fanout, N_peaks)):
            fingerprint.append((peak_frequencies[n], peak_frequencies[j], peak_times[j] - peak_times[n]))
    return fingerprint   


###########################


def mp3ToDAS(song_list):
    """ Parameters
        ----------
        song_list : array of songs
        Returns
        ----------
        audio_data_mp3 : a numpy array that contains the digitized audio data"""
    #songs = [Path(".")/song_list]
    #local_song_path = songs[0]
    samples, fs = librosa.load('/Users/caseygoldstein/Desktop/james_arthur_say_you_wont_let_go.mp3'
, sr=44100, mono=True, duration=11)

    sampling_rate = 44100
    quantizing_bits = 16
    #audio_data_mp3 = song_to_digital('/Users/caseygoldstein/Desktop/james_arthur_say_you_wont_let_go.mp3', sampling_rate, quantizing_bits)
    #return audio_data_mp3
    print('done!')
    samples = samples *(2**15)
    return samples

    

    # needs revision - revise based on where we will have mp3 files



###########################

def find_peaks(spectrogram, fp=FOOTPRINT_BASIC, cutoff=0.0):
    filtered_spectrogram = maximum_filter(spectrogram, footprint=fp)

    spectrogram_peaks = (spectrogram == filtered_spectrogram)
    spectrogram_peaks *= (spectrogram >= cutoff)

    time, freq = np.where(spectrogram_peaks)
    return time, freq

###########################

def DigToSpec(audioData):
    print('done!')
    return mlab.specgram(audioData, NFFT=4096, Fs=44100,window=mlab.window_hanning,noverlap=4096 // 2)
    
 
###########################  

def turn_off_ticks(ax):
    for tic in ax.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.label1On = tic.label2On = False
    for tic in ax.yaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.label1On = tic.label2On = False

def analog_to_digital(fig, ax, sampling_rate, quantizing_bits, digital_graph = False):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import logistic
        

    x                   = 2. # s.
    analog_time         = np.linspace (0, x, int(10e5)) # s.

    sample_number       = x * sampling_rate 
    sampling_time       = np.linspace (0, x, int(sample_number))

    quantizing_levels   = 2 ** quantizing_bits / 2
    quantizing_step     = 1. / quantizing_levels

    def analog_signal (time_point):
        return 1 / (1 + np.exp(-10*(time_point - 1)))  #logistic.cdf(time_point)


    sampling_signal     = analog_signal (sampling_time);
    quantizing_signal   = np.round (sampling_signal / quantizing_step) * quantizing_step

    if not digital_graph:
        ax.plot (analog_time, analog_signal (analog_time))
        ax.stem (sampling_time, quantizing_signal, markerfmt='r_', linefmt = ' ', basefmt = ' ')
        ax.set_title("Analog to digital signal conversion")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
    else:
        new_l = len(analog_time) / len(quantizing_signal)
        new_y = []
        for i in range(len(quantizing_signal)):
            new_y += [quantizing_signal[i]] * int(new_l)
        
        ax.plot(analog_time, analog_signal(analog_time))
        ax.plot(analog_time, new_y, alpha=0.7)
        turn_off_ticks(ax)



def song_to_digital(local_song_path = None, sampling_rate = 40, quantizing_bits = 4):
    import urllib
    import librosa
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()
    
    if local_song_path is None:
        song_path = 'test_song.mp3'
    else: 
        song_path = local_song_path
    
    samples, fs = librosa.load(song_path, sr=44100, mono=True)
    samples = samples[:11 * 44100]
    time = np.linspace(0,11, 11 * 44100)
    
    ax.plot(time[::10], samples[::10])
    
    skip = int(len(samples) / (11 * sampling_rate))
    sampling_signal     = samples[::skip]

    quantizing_levels   = 2 ** quantizing_bits / 2
    quantizing_step     = 1. / quantizing_levels
    
    quantizing_signal   = np.round (sampling_signal / quantizing_step) * quantizing_step;

    new_l = len(time) / len(quantizing_signal)
    new_y = []
    for i in range(len(quantizing_signal)):
        new_y += [quantizing_signal[i]] * int(new_l)

    ax.plot (time, new_y);
    ax.set_title("Analog to digital signal conversion")
    ax.set_xlabel("Time(s)")
    ax.set_ylabel("Amplitude")


###########################  

    
 
    
#with open("/Users/caseygoldstein/Desktop/trumpet_copy.txt", 'r') as R:
  #  trumpet_audio = np.asarray([int(i.split("\n")[0]) for i in R if i.split("\n")[0] is not ''])

sayyouwontletgo = mp3ToDAS('test')
testspec = DigToSpec(sayyouwontletgo)
testspec = testspec[0]
print('testspec shape: ' + str(testspec.shape))
print('done!')
threshold = findthreshold(testspec)
print('done!')



OurFirstFingerprint = generate_fingerprint(testspec,fp=FOOTPRINT_BASIC,cutoff=-threshold,fanout=30)

#print(OurFirstFingerprint)
print(len(OurFirstFingerprint))