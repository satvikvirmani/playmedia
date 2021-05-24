# playmedia

## Install
`pip install playmedia`

------------

**playmedia** python package helps you easily play and control media files. It uses multithreading technology ( playback run in a different thread ). It means after calling `play_single( filepath )` or `play_multiple( directoryPath, shuffle )` execution of program does not stop.

Example :-
```python
from playmedia import *

play_single("C:\\Users\\Satvik\\Music\\Why do I.mp3")
print("This is printed as soon as play_single() is called. It does not wait for song to finish")

#Output :
This is printed as soon as play_single() is called. It does not wait for song to finish
```
It supports almost all popular formats :-
- .m4a
- .flac
- .mp3
- .mp4
- .wav
- .wma
- .aac
- .mkv

It has 2 major functions :-
1. play_single()
2. play_multiple()

------------

### 1. play_single( filepath )
`play_single( filepath )`
- filepath ->full path of loaction of media eg.(**"C:\\\Users\\\Satvik\\\Music\\\Why do I.mp3"**). Double backslash( \\\ ) should be used as using others might throw unicode error.

It has 3 method inside it.
- `pause_single()` - Pauses the song. (calling `pause_single()` again resumes it)

- `set_volume_single(vol)` - Sets the volume of player to vol%. Eg. `set_volume_single(60)` sets volume to 60%

- `stop_single()` - Stops playing . Only it should be called to stop playing. Using other techniques might stop playing but not stop the thread

Example Usage :-
```python
from playmedia import *

play_single("C:\\Users\\Satvik\\Music\\Why do I.mp3")
#playing started
pause_single()
#pauses
pause_single()
#calling  pause_single() again resumes the song
set_volume_single(60)
#sets volume to 60%
stop_single()
#stops playing the song

```

------------

### 2. play_multiple( directoryPath, shuffle )
`play_multiple( directoryPath, shuffle )`
- directoryPath ->full path of directory containing multiple media eg.(**"C:\\\Users\\\Satvik\\\Music\\\"**). Double backslash( \\\ ) should be used as using others might throw unicode error. Also double backslash( \\\ ) at the end is neccesary.
- shuffle ->**True** if you want the songs to be played in random order else **False**

It has 5 method inside it.
- `pause_multiple()` - Pauses the song. (calling `pause_multiple()` again resumes it)

- `set_volume_multiple(vol)` - Sets the volume of player to vol%. Eg. `set_volume_multiple(60)` sets volume to 60%

- `next_multiple()` - Plays next song in the list

- `previous_multiple` - Plays previous song in the list

- `stop_multiple()` - Stops playing . Only it should be called to stop playing. Using other techniques might stop playing but not stop the thread

Example Usage:-
```python
from playmedia import *

play_multiple("C:\\Users\\Satvik\\Music\\", False)
#started playing
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

------------

## 🤝Contributing
Contributions, issues and feature requests are welcome!
Feel free to check [Bug Tracker](https://github.com/SatvikVirmani/playmedia/issues "issues") page.
To submit improvements or features check [Pull Requests](https://github.com/SatvikVirmani/playmedia/pulls "Pull Requests")