from microphone import record_audio

import numpy as np
from songmatch.audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks
import urllib
import librosa
import matplotlib.pyplot as plt
from IPython.display import Audio
from pathlib import Path


def mp3ToDAS(song_name):
    """ Parameters
        ----------
        song_list : array of songs


        Returns
        ----------
        audio_data_mp3 : a numpy array that contains the digitized audio data"""
    local_song_path = Path("./songs/" + song_name)
    samples, fs = librosa.load(local_song_path, sr=44100, mono=True)
    audio_data_mp3 = samples * (2**15)
    return audio_data_mp3

def mp3ToDAS2(song_list):
    """ Parameters
        ----------
        song_list : array of songs


        Returns
        ----------
        audio_data_mp3 : a numpy array that contains the digitized audio data"""
    songs = [Path("./songs/" + song) for song in song_list]
    local_song_path = songs[0]
    samples, fs = librosa.load(local_song_path, sr=44100, mono=True, duration=10)
    audio_data_mp3 = samples * (2**15)
    return audio_data_mp3