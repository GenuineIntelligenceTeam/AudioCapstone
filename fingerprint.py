import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure

FOOTPRINT_BASIC = generate_binary_structure(rank=2, connectivity=1)

"""
Find a 2xN list of all peaks within a given spectrogram.

Parameters
----------
spectrogram: ndarray
    The input spectrogram to use

fp: ndarray
    The footprint array to use for filtering

cutoff: float
    Cutoff pixel value to use to filter the background.

Returns
-------
time, freq: ndarray, ndarray
    NDarrays of indices for the time and frequency of each peak.
"""
def find_peaks(spectrogram, fp=FOOTPRINT_BASIC, cutoff=0.0):
    filtered_spectrogram = maximum_filter(data, footprint=fp)

    spectrogram_peaks = (spectrogram == filtered_spectrogram)
    spectrogram_peaks *= (spectrogram >= cutoff)

    time, freq = np.where(spectrogram_peaks)
    return peaks_list

"""
Compute a fingerprint of relative distances between peaks in a given spectrogram.

Parameters
----------
spectrogram: ndarray
    The input spectrogram to use

fp: ndarray
    The footprint array to use for filtering

cutoff: float
    Cutoff pixel value to use to filter the background.

fanout: int
    Value of the fanout to connect each element of the fingerprint to others.

Returns
-------
fingerprint: array
    Array of 3-tuples representing frequencies and their relative time differences
"""
def generate_fingerprint(spectrogram, fp=FOOTPRINT_BASIC, cutoff=0.0, fanout=30):
    peak_times, peak_frequencies = find_peaks(spectrogram, fp, cutoff)

    N_peaks = len(peak_times)

    fingerprint = []
    for n in range(N_peaks):
        for j in range(n + 1, n + 1 + fanout):
            fingerprint.append((peak_frequencies[n], peak_frequencies[j], peak_times[j] - peak_times[n]))

    return fingerprint