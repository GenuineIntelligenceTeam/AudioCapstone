from songmatch.mp3toDAS import mp3ToDAS, mp3ToDAS2
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher
from songmatch.addfingerprintstodatabase import addfingerprintstodatabase
from songmatch.songbase import songbase
import songmatch

import numpy as np

song_list = songbase

for i, element in enumerate(song_list):
    audio_data = mp3ToDAS(song_list)
    S = DigToSpec(audio_data)
    threshold = findthreshold(S)
    fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((50,50)))
    addfingerprintstodatabase(fingerprint, i)

    audio_data2 = mp3ToDAS2(song_list)
    S = DigToSpec(audio_data2)
    threshold = findthreshold(S)
    fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((50,50)))
    print(songbase[FingerprintMatcher(songmatch.songDatabase, fingerprint)])