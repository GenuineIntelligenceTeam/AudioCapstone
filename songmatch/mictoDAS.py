from microphone import record_audio

import numpy as np

def micToDAS(listen_time):
    """ Parameters
        ----------
        listen_time : the time in seconds that microphone records


        Returns
        ----------
        audio_data : a numpy array that contains the digitized audio data"""

    byte_encoded_signal, sampling_rate = record_audio(listen_time)
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in byte_encoded_signal])
    return audio_data
