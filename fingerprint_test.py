import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure

from fingerprint import generate_fingerprint

from micToDAS import micToDAS
from DigToSpec import DigToSpec

import datetime

with open("data/trumpet.txt", 'r') as R:
    trumpet_audio = np.asarray([int(i) for i in R])
    
sampling_rate = 44100 # sampling rate in Hz

"""
fig, ax = plt.subplots()

S, freqs, times, im = ax.specgram(trumpet_audio, NFFT=4096, Fs=sampling_rate,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)
fig.colorbar(im)

ax.set_xlabel("Time (sec)")
ax.set_ylabel("Frequency (Hz)")
ax.set_title("Spectrogram of Trumpet")
ax.set_ylim(0, 6000)
"""

audio_data = micToDAS(30)
S, _, _ = DigToSpec(audio_data)

print("starting fing")
_start_time = datetime.datetime.now()
u = generate_fingerprint(S, fp=np.ones((10,10)))
print("stopping", (datetime.datetime.now() - _start_time).total_seconds())
print(len(u))