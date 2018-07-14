from songmatch.mp3toDAS import mp3ToDAS, mp3ToDAS2
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher
from songmatch.addfingerprintstodatabase import addfingerprintstodatabase
from songmatch.songbase import songbase
import songmatch

from scipy.ndimage.morphology import iterate_structure, generate_binary_structure

import numpy as np
import pickle

def train_all_songs():
    song_list = songbase

    for song_id, song in enumerate(songbase):
        audio_data = mp3ToDAS(song)
        S = DigToSpec(audio_data)
        threshold = findthreshold(S)
        print("STARTING FINGERPRINT GENERATION ", song_id)
        fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((30,30)))
        addfingerprintstodatabase(fingerprint, song_id)

    with open('database.pickle', 'wb') as handle:
        pickle.dump(songmatch.songDatabase, handle)
