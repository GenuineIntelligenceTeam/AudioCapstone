import matplotlib.mlab as mlab
import numpy as np

""" Converts from a digital audio data to a spectrogram
        
        Parameter
        ----------
        audioData : List of encoded audio file's data 
        
        Returns
        --------
        S: 2d Array of Frequency and Time
"""
def DigToSpec(audioData):
    S, _, _ = mlab.specgram(audioData, NFFT=4096, Fs=44100,window=mlab.window_hanning,noverlap=4096 // 2)
    S += 1e-20
    return np.log(S).transpose()
