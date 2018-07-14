from songmatch.mp3toDAS import mp3ToDAS
from songmatch.mictoDAS import micToDAS
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher
from songmatch.addfingerprintstodatabase import addfingerprintstodatabase
from songmatch.songbase import songbase
from microphone import record_audio

from scipy.ndimage.morphology import iterate_structure, generate_binary_structure

import numpy as np
import pickle

with open('database.pickle', 'rb') as handle:
    database = pickle.load(handle)

def match_recording(time):
    audio_data = micToDAS(time)
    S = DigToSpec(audio_data)
    threshold = findthreshold(S)
    fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((30,30)))
    print(songbase[FingerprintMatcher(database, fingerprint)])



