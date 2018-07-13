import numpy as np
from collections import defaultdict, Counter
import operator

def FingerprintMatcher(database, sampleData):
    idk = defaultdict(list)
    for index, item in enumerate(sampleData):
        for key in database:
            if key == item:
                for i in database.get(key):
                    idk[(i[0],np.abs(index-i[1]))].append(1)
    return max(idk.items(), key=operator.itemgetter(1))[0][0]

    


