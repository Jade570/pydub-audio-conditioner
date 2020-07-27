import os
import numpy as np
from pydub import AudioSegment

def downsample(input_wav, resample_sr): #write the samplerate you want to resample as
    audio = AudioSegment.from_wav(input_wav)
    audio = audio.set_frame_rate(resample_sr)
    return audio

def splitsize(songnum, trimnum, audio, t1, size):
    name = "../2008trim/"+str(songnum)+"-"+str(trimnum)+".wav"
    t2 = t1 + size
    newAudio = audio
    newAudio = newAudio[t1:t2]
    newAudio.export(name, format="wav")
    t1 = t2
    return t1

def splitaudio(songnum, trimnum, audio):
    t1 = 0
    t2 = 0
    n = trimnum
    while t1+5000 < len(audio): #while the file is not at the end
        t1 = splitsize(songnum, n, audio, t1, 5000) #split by 5seconds
        n += 1 

song = 0
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".wav"):
            splitaudio(song, 0, downsample(filename, 16000))
            print(song)
            song += 1
