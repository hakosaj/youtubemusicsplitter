import librosa

y,sr = librosa.load("wav_files/doiwannaknow.wav",sr=22050)


#Around 5 million points of sampled time serie data
print(y.shape)
#Sample rate, ere 22050
print(sr)

mfccs = librosa.feature.mfcc(y=y, sr=sr)

print(type(mfccs))
print(mfccs.shape)