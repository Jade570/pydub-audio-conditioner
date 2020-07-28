import os
import sys
import argparse
from pydub import AudioSegment

DIR = "./"
SAMPLERATE = 24000
BITRATE = 16
SEC = 5000
EXTENSION = "wav"
#AudioSegment.converter = 'path/to/ffmpeg.exe'

def get_arguments():
    parser = argparse.ArgumentParser(description='Wav file conditioner for training dataset')
    parser.add_argument('--targetdir', type=str, default=DIR, help='The directory you will store the conditioned files at. Default: '+DIR+'.')
    parser.add_argument('--sourcedir', type=str, default='.', help='The directory you have your original wave files at. Default: current directory.')
    parser.add_argument('--samplerate', type=int, default=SAMPLERATE, help='Sample rate you want to condition files as. Default: '+str(SAMPLERATE)+'.')
    parser.add_argument('--bitrate', type=int, default=BITRATE, help='Bit rate you want to condition files as. Defualt: '+str(BITRATE)+'.')
    parser.add_argument('--seconds', type=int, default=SEC, help='How many seconds you want to trim files as. Default: '+str(SEC)+'.')
    parser.add_argument('--extension', type=str, default=EXTENSION, help='Extension you want the conditioned files to have, Default :'+EXTENSION+'.')
    return parser.parse_args()


def downsample(input_wav, resample_sr): #write the samplerate you want to resample as
    args = get_arguments()

    audio = AudioSegment.from_wav(input_wav)
    audio = audio.set_frame_rate(resample_sr)
    return audio

def splitsize(songnum, trimnum, audio, t1, size):
    args = get_arguments()

    _dir = args.targetdir
    _extension = args.extension
    _bitrate = args.bitrate
    if _dir.endswith('/'):
        name = _dir+str(songnum)+"-"+str(trimnum)+"."+_extension
    else:
        name = _dir+'/'+str(songnum)+"-"+str(trimnum)+"."+_extension
    t2 = t1 + size
    newAudio = audio
    newAudio = newAudio[t1:t2]
    newAudio.export(name, format=_extension, bitrate=_bitrate)
    t1 = t2
    return t1

def splitaudio(songnum, trimnum, audio):
    args = get_arguments()

    t1 = 0
    t2 = 0
    n = trimnum
    seconds = args.seconds
    while t1+seconds < len(audio): #while the file is not at the end
        t1 = splitsize(songnum, n, audio, t1, seconds)
        n += 1 

def main():
    args = get_arguments()

    song = 0
    _samplerate = args.samplerate
    _source = args.sourcedir
    _ext = args.extension
    for root, dirs, files in os.walk(_source):
        for filename in files:
            if filename.endswith("."+_ext):
                if _source.endswith('/'):
                    splitaudio(song, 0, downsample(_source+filename, _samplerate))
                    print(song)
                    song += 1
                else:
                    splitaudio(song, 0, downsample(_source+'/'+filename, _samplerate))
                    print(song)
                    song += 1


if __name__ == '__main__':
    main()
