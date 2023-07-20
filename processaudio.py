import librosa
import numpy as np
import os
import pickle

g=os.listdir("wav_files")

spectrals=[]
for vidfile in g:

    dr=librosa.get_duration(path=f"wav_files/{vidfile}")
    y,sr = librosa.load(f"wav_files/{vidfile}",sr=10000/dr)



    #25k  points of sampled time serie data
    print(f"Sampling data: {y.shape}")
    print(f"Sample rate: {sr}")
    mfccs = librosa.feature.mfcc(y=y, sr=sr)

    print(mfccs.shape)

    mfccs_mean = np.mean(mfccs, axis=0)[::2]
    mfccs_max = np.max(mfccs, axis=0)[::2]

    print(mfccs_max.shape)
    print(mfccs_mean.shape)


    zero_crossings = librosa.zero_crossings(y, pad=False)
    print(np.array((sum(zero_crossings))))
    song_characteristics=np.concatenate((mfccs_mean,mfccs_max))
    song_characteristics=np.concatenate((song_characteristics,[sum(zero_crossings)]))
    spectrals.append(song_characteristics)
    #https://towardsdatascience.com/extract-features-of-music-75a3f9bc265dnp.array(sum(zero_crossings))
spectrals=np.array(spectrals)
print(spectrals.shape)
with open('spectrals.pickle', 'wb') as file:
    pickle.dump(spectrals,file)