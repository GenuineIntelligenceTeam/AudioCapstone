import matplotlib.mlab as mlab

""" Converts from a digital audio data to a spectrogram
        
        Parameter
        ----------
        audioData : List of encoded audio file's data 
        
        Returns 
        ----------
        Tuple of Spectrogram, Frequency, and Time
                                                        """
                                                            

def DigToSpec(audioData):
    return mlab.specgram(audioData, NFFT=4096, Fs=44100,window=mlab.window_hanning,noverlap=4096 // 2)
