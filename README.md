# pydub-audio-conditioner
Audio conditioner for making training dataset for Wavenet training

## Dependencies

```Shell
$ brew install ffmpeg

```

## How To Start
```Shell
$ git clone https://github.com/Jade570/pydub-audio-conditioner.git

$ cd pydub-audio-conditioner

$ pip install -r requirements.txt

$ python wav_conditioner.py --sourcedir=/path/to/original/sources --

```

## Arguments
There are `--targetdir`, `--sourcedir`, `--samplerate`, `--bitrate`, `--seconds`, `--extension` arguments you can change in the terminal while executing this project.  
example:
```shell
$ python wav_conditioner.py
#every arguments are set to default

$ python wav_conditioner.py --seconds=15000
#split audio files into 15000milliseconds(1.5seconds)
```

### 1. `--targetdir`  
The directory you will store the conditioned files at.  
Default: `current directory`

### 2. `--sourcedir` 
The directory you have your original wave files at.  
Default: `current directory`

### 3. `--samplerate`
Sample rate you want to condition files as.  
Default: `24000`

### 4. `--bitrate`
Bit rate you want to condition files as.  
Default: `16`

### 5. `--seconds`
How many milliseconds you want to split files as.  
Default: `5000`

### 6. `--extension`
Extension you want the conditioned files to have.   
Default: `wav`
