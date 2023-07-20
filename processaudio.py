import librosa
import numpy as np

dr=librosa.get_duration(filename="wav_files/afterglow.wav")
y,sr = librosa.load("wav_files/afterglow.wav",sr=10000/dr)



#Around 26k  points of sampled time serie data
print(f"Sampling data: {y.shape}")
#Sample rate, ere 100
print(f"Sample rate: {sr}")
mfccs = librosa.feature.mfcc(y=y, sr=sr)

print(mfccs.shape)

mfccs_mean = np.mean(mfccs, axis=0)
mfccs_max = np.max(mfccs, axis=0)

print(mfccs_max.shape)
print(mfccs_mean)
print(mfccs_max)


#zero_crossings = librosa.zero_crossings(y[6000:6500], pad=False)
#print(sum(zero_crossings))
#https://towardsdatascience.com/extract-features-of-music-75a3f9bc265d