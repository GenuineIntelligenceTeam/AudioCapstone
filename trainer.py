audio_data = micToDAS(8)
spectrogram = DigToSpec(audio_data)
time, freq = find_peaks(spectrogram, fp = np.ones((3,3)), cutoff = 0)
