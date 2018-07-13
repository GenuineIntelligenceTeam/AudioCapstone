from songmatch.mp3toDAS import mp3ToDAS
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher
from songmatch.addfingerprintstodatabase import addfingerprintstodatabase

import numpy as np

print("Welcome to SongMatch - Trainer. Enter song file name: ")
song_name = input()

song_list = [song_name]

print("Enter song ID in database: ")
song_id = int(input())

audio_data = mp3ToDAS(song_list)
S = DigToSpec(audio_data)
threshold = findthreshold(S)
print("STARTING FINGERPRINT GENERATION")
fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((50,50)))
addfingerprintstodatabase(fingerprint, song_id)
