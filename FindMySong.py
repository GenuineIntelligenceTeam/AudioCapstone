from songmatch.mp3toDAS import mp3ToDAS
from songmatch.mictoDAS import micToDAS
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher
from songmatch.addfingerprintstodatabase import addfingerprintstodatabase
from songmatch.songbase import songbase
import songmatch
from microphone import record_audio
import numpy as np
import pickle
with open('database.pickle', 'rb') as handle:
    database = pickle.load(handle)
print(set(x[0] for x in database.values()))

print("Welcome to SongMatch - Trainer. Enter recording time: ")

time = int(input())
audio_data = micToDAS(time)
S = DigToSpec(audio_data)
threshold = findthreshold(S)
fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((20,20)))
print(songbase[FingerprintMatcher(database, fingerprint)])




