<p align="center">
    <h1 align="center">playmedia</h1>
</p>

> ### A python module to play and control media files.

<p align="center">
    <a href="">
        <img src="https://img.shields.io/badge/Made%20by%20Satvik%20Virmani-000000?style=for-the-badge">
    </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
  <img src="https://img.shields.io/github/issues/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
</p>

## Installation

```python
pip install playmedia
```

## Dependencies

* [VLC Media Player](https://sourceforge.net/projects/vlc/)

## Usage

1. ### class File
   You can initiate the File class with the path of the media file as argument.
   ```python
    File("path/to/the/media/file")
    ```
    
    * #### start() 
    ##### This method starts the playback
    args = None, return = string

    * #### pause(status) 
    ##### This method pauses/resumes the playback
    args = [status: boolean], return = string

    * #### mute(status) 
    ##### This method mutes/unmutes the playback
    args = [status: boolean], return = string

    * #### set_volume(vol) 
    ##### This method set the volume of the playback
    args = [vol: int], defaults = [vol: 100], return = string

    * #### stop() 
    ##### This method stops the playback
    args = None, return = None

    * #### meta(tag) 
    ##### This method returns the meta data of the media
    args = [tag: string], defaults = [tag: "Date"], return = string

    * #### edit_meta(tag, new_value) 
    ##### This method changes the meta data values
    args = [tag: string, new_value: string], return = string

    Supported tags = Actors, Album, AlbumArtist, Artist, ArtworkURL, Copyright, Date, Description, Director, DiscNumber, DiscTotal, EncodedBy, Episode, Genre, Language, NowPlaying, Publisher, Rating, Season, Setting, ShowName, Title, TrackID, TrackNumber, TrackTotal, URL

    ```python
    instance = File("path/of/the/media/file/Why do I?.mp3")
    instance.start() # Returns Now playing Why do I?
    instance.pause(True) # Returns Paused
    instance.mute(False) # Returns Unmuted
    instance.set_volume(75) # Returns Volume set to 75%
    instance.meta("Artist") # Returns Artist: Unknown Brain
    instance.edit_meta("Album","playmedia") # Changed Album to playmedia
    instance.stop()
    ```

    > Note: Statements are returned not printed. To print the returned values use `print(instance.set_volume(75))`
    * #### stop() 
    args = None, return = None
2. ### class Files
   You can initiate the File class with either the path of the dirctory containing files or list with paths of the media files.
   ```python
    Files("path/to/the/dirctory/containing/media/file")
    or
    Files(["path/to/media/file/1", "path/to/media/file/2"])
    ```

    * #### get_list() 
    ##### This method returns a dictionary with index as keys and files as values 
    args = None, return = dictionary

    * #### start() 
    ##### This method starts the playback in order
    args = None, return = dictionary

    * #### play_at_index(index) 
    ##### This method starts the playback of the media file at the given index
    args = [index: int], return = string

    * #### pause(status) 
    ##### This method pauses/resumes the playback
    args = [status: boolean], return = string

    * #### next() 
    ##### This method skips the current media and plays the next one
    args = None, return = string

    * #### previous() 
    ##### This method plays the previous media
    args = None, return = string

    * #### mute(status) 
    ##### This method mutes/unmutes the playback
    args = [status: boolean], return = string

    * #### set_volume(vol) 
    ##### This method set the volume of the playback
    args = [vol: int], defaults = [vol: 100], return = string

    * #### stop() 
    ##### This method stops the playback
    args = None, return = None

    * #### current_meta(tag) 
    ##### This method returns the meta data of the currently playing media
    args = [tag: string], defaults = [tag: "Date"], return = string

    > Note: A media should be playing when this method is called. Either call start(), play_at_index(index) before otherwise it raises a IndexError.

    Supported tags = Actors, Album, AlbumArtist, Artist, ArtworkURL, Copyright, Date, Description, Director, DiscNumber, DiscTotal, EncodedBy, Episode, Genre, Language, NowPlaying, Publisher, Rating, Season, Setting, ShowName, Title, TrackID, TrackNumber, TrackTotal, URL

    * #### current_time() 
    args = None, return = dictionary

    ```python
    instance = File("path/to/the/dirctory/containing/media/file")
    instance.get_list() # Returns {0: 'File 1.mp3', 1: 'File 2 .mp4', 2: 'File 3.wav'}
    instance.start() # Returns {0: 'File 1.mp3', 1: 'File 2 .mp4', 2: 'File 3.wav'}
    instance.stop()
    instance.play_at_index(1) # Returns Now playing File 2
    instance.pause(True) # Returns Paused
    instance.mute(False) # Returns Unmuted
    instance.set_volume(75) # Returns Volume set to 75%
    instance.current_meta("Artist") # Returns Artist: "Artist of File 2"
    instance.current_time("Album","playmedia") # Returns {"Current time": '98.63s'}
    ```
    
    > Note: Statements are returned not printed. To print the returned values use `print(instance.set_volume(75))`


#### Supported Files
1. '.m4a'
2. '.flac'
3. '.mp3'
4. '.mp4'
5. '.wav'
6. '.wma'
7. '.aac'
8. '.mkv'

## Author

### Satvik Virmani

<a href="https://twitter.com/satvikvirmani">
    <img src="https://img.shields.io/twitter/follow/satvikvirmani?color=000000&logo=twitter&logoColor=FFFFFF&style=for-the-badge">
</a>

## Contributions

Contributions, issues and feature requests are welcome!
Feel free to check [issues](https://github.com/satvikvirmani/playmedia/issues) page.

## Show your support

Give a ⭐️ if this project helped you!