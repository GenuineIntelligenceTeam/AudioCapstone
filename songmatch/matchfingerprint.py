import numpy as np
from collections import defaultdict, Counter
import operator

'''
Matches sample song's fingerprint and database's fingerprint

Parameters
----------
database: Dictionary with keys of (f1,f2,delta time) and values of [(song_name,t),...]
sampleData: List of tuples ((f1,f2, delta time), time of peak)

Returns
-------
String of song name

'''

def gen_keys(database, sampleData):
     for item, _ in sampleData: #Loops through the sample audio and seperates the index and item (f1, f2, delta time)
        val = database.get(item)
        if val is not None:
            yield val

def FingerprintMatcher(database, sampleData):
    count = Counter(gen_keys(database, sampleData)) #
    return count.most_common()[0][0][0]

def fp_match_old(database, sampleData):
    idk = defaultdict(list)
    for item, peakTime in sampleData: #Loops through the sample audio and seperates the index and item (f1, f2, delta time)
        for key in database: #Gets the key (f1, f2, delta time) 
            if key == item: #Checks if a key from database matches the item
                i = database.get(key)
                idk[(i[0],np.abs(peakTime-i[1]))].append(1)
    return max(idk.items(), key=operator.itemgetter(1))[0][0] #Finds the song with the most timing similarities
    

    


