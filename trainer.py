from songmatch.mp3toDAS import mp3ToDAS
from songmatch.digtospec import DigToSpec
from songmatch.findthreshold import findthreshold
from songmatch.genfingerprint import generate_fingerprint
from songmatch.matchfingerprint import FingerprintMatcher

import numpy as np

song_list = ["ComfortablyNumb.mp3"]

audio_data = mp3ToDAS(song_list)
S = DigToSpec(audio_data)
threshold = findthreshold(S)
print("STARTING FINGERPRINT GENERATION")
fingerprint = generate_fingerprint(S, cutoff=threshold, fp=np.ones((50,50)))

