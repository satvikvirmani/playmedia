"""
# PlayMedia

## Usage
### Install

Install the [PyPI package](https://pypi.org/project/playmedia/):

    pip install playmedia


playmedia python package helps you easily play and control media files. It uses multithreading technology ( playback run in a different thread ). It means after calling play_single( filepath, vol ) or play_multiple( directoryPath, vol, shuffle ) execution of program does not stop.

### Functions

#### 1. play_single( filepath, vol )

play_single( filepath ,vol )

    filepath -> full path of location of media eg.("C:\\Users\\Satvik\\Music\\Why do I.mp3"). Double backslash( \\ ) should be used as using others might throw unicode error.
    vol -> Sets the volume of player to vol%

It has 3 method inside it.

    pause_single() - Pauses the song. (calling pause_single() again resumes it)

    set_volume_single(vol) - Sets the volume of player to vol%. Eg. set_volume_single(60) sets volume to 60%

    stop_single() - Stops playing . Only it should be called to stop playing. Using other techniques might stop playing but not stop the thread

Example: 

```py
from playmedia import *

play_single("C:\\Users\\Satvik\\Music\\Why do I.mp3", 100)
#playing started at 100% volume
pause_single()
#pauses
pause_single()
#calling  pause_single() again resumes the song
set_volume_single(60)
#sets volume to 60%
stop_single()
#stops playing the song
```
### 2. play_multiple( directoryPath, shuffle )

play_multiple( directoryPath, vol,  shuffle )

    directoryPath -> full path of directory containing multiple media eg.("C:\\Users\\Satvik\\Music\"). Double backslash( \\ ) should be used as using others might throw unicode error. Also double backslash( \\ ) at the end is neccesary.
    vol -> Sets the volume of player to vol%
    shuffle -> True if you want the songs to be played in random order else False

It has 5 method inside it.

    pause_multiple() - Pauses the song. (calling pause_multiple() again resumes it)

    set_volume_multiple(vol) - Sets the volume of player to vol%. Eg. set_volume_multiple(60) sets volume to 60%

    next_multiple() - Plays next song in the list

    previous_multiple - Plays previous song in the list

    stop_multiple() - Stops playing . Only it should be called to stop playing. Using other techniques might stop playing but not stop the thread

Example:

```py
from playmedia import *

play_multiple("C:\\Users\\Satvik\\Music\\",100 , False)
#started playing at 100% volume
pause_multiple()
#pauses the current song
pause_multiple()
#calling  pause_multiple() again resumes the current song
next_multiple()
#plays next song in the list
previous_multiple()
#plays previous song in the list
set_volume_multiple(60)
#sets volume to 60%
stop_multiple()
#stops playing the songs
```


🤝Contributing

Contributions, issues and feature requests are welcome! Feel free to check [Bug Tracker](https://github.com/SatvikVirmani/playmedia/issues) page. To submit improvements or features check [Pull Requests](https://github.com/SatvikVirmani/playmedia/pulls)


"""
# Documentation (in visual code) created and updated to include "vol" option, all based on the original documentation (By Rockett68)  

from threading import Thread
import vlc, os, random, time

stopped_multiple = False
stopped_single = False
single_instance = None
multiple_instance = None

class SinglePlayer:
    def __init__(self, file, vol):
        self.player = vlc.MediaPlayer()
        self.player.audio_set_volume(vol)
        self.media = vlc.Media(file)
        self.skip = False

    def pause(self):
        self.player.pause()
    
    def stop(self):
        self.player.stop()
        
    def set_volume(self, vol):
        self.player.audio_set_volume(vol)

    def start_playing(self):
        self.player.set_media(self.media)
        self.player.play()

class MultiplePlayer:
    def __init__(self, path, vol, shuffle):
        self.player = vlc.MediaListPlayer()
        self.list = vlc.MediaList()
        self.player.get_media_player().audio_set_volume(vol)
        self.path = path
        self.shuffle = shuffle

    def pause(self):
        self.player.pause()
    
    def stop(self):
        self.player.stop()
        
    def set_volume(self, vol):
        self.player.get_media_player().audio_set_volume(vol)

    def next(self):
        self.player.next()

    def previous(self):
        self.player.previous()

    def start_playing(self):
        formats = [".m4a", ".flac", "mp3", "mp4", "wav", "wma", "aac", ".mkv"]
        files = []
        for file in os.listdir(self.path):
            for format in formats:
                if file.endswith(format):
                    files.append(self.path+file)
                    break
        for i in range(files.__len__()):
            if self.shuffle:
                fileMRL = files[random.randint(0, len(files)-1)]
                self.list.add_media(fileMRL)
                files.remove(fileMRL)
            else:
                fileMRL = files[i]
                self.list.add_media(fileMRL)
        self.player.set_media_list(self.list)
        self.player.play()

def play_flow_multiple(path, vol, shuffle):
    global multiple_instance
    multiple_instance = MultiplePlayer(path, vol, shuffle)
    multiple_instance.start_playing()
    global stopped_multiple
    while True:
        if stopped_multiple:
            break
def play_multiple(path,vol,shuffle=False):
    thread_a = Thread(target=play_flow_multiple, args=(path,vol,shuffle))
    thread_a.start()
def pause_multiple():
    global multiple_instance
    multiple_instance.pause()
def stop_multiple():
    global stopped_multiple, multiple_instance
    multiple_instance.stop()
    stopped_multiple = True
def set_volume_multiple(vol):
    time.sleep(1)
    global multiple_instance
    multiple_instance.set_volume(vol)
def next_multiple():
    global multiple_instance
    multiple_instance.next()
def previous_multiple():
    global multiple_instance
    multiple_instance.previous()

def play_flow_single(url, vol, bugFix):
    global single_instance
    single_instance = SinglePlayer(url, vol)
    single_instance.start_playing()
    global stopped_single
    while True:
        if stopped_single:
            break
def play_single(url, vol, bugFix=False):
    thread_b = Thread(target=play_flow_single, args=(url, vol, bugFix))
    thread_b.start()
def pause_single():
    global single_instance
    single_instance.pause()
def stop_single():
    global stopped_single, single_instance
    single_instance.stop()
    stopped_single = True
def set_volume_single(vol):
    time.sleep(1)
    global single_instance
    single_instance.set_volume(vol)