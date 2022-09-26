from ctypes import ArgumentError

# importing the classes from python-vlc
from vlc import Media, MediaPlayer, Meta

# importing Path class from pathlib
from pathlib import Path

# importing pretty-errors module (This module is not accessed but importing it formats the errors raised and display them nicely in the terminal)
import pretty_errors


class File:

    def __init__(self, arg: str) -> None:  # defining the init function

        self.file_path = arg  # setting the path variable equal to the argument

        # If the argument is not a string then we raise a TypeError
        if type(arg) != str:
            raise TypeError("The argument should be a string.")

        # We first check if the given path exists
        if Path(self.file_path).exists():
            
            # Types of media files supported by libvlc
            supported_files = ['.m4a', '.flac', '.mp3',
                           '.mp4', '.wav', '.wma', '.aac', '.mkv']
            
            #Add file only if the file is supported
            if Path(self.file_path).suffix in supported_files:
                # setting media variable equal to the Media Class of python-vlc
                self.media = Media(self.file_path)
                # setting player variable equal to the MediaPlayer Class of python-vlc
                self.player = MediaPlayer()
            else:
                raise FileNotFoundError(f"The extension {Path(self.file_path).suffix} is not supported. Check the documentation for the list of valid media files.")
        else:
            # If the file does not exist then we raise a FileNotFoundError
            raise FileNotFoundError("No file found for the given path.")

        self.set_file()  # We call the set_file method initially

    def set_file(self):  # defining set_file function
        # Setting the media in the media player
        self.player.set_media(self.media)

        # Resetting all settings
        self.player.audio_set_volume(100)
        self.player.set_pause(False)
        self.player.audio_set_mute(False)

    def meta(self, tag: str = "Date") -> str:  # defining the meta function
        # We need to first parse media to get meta data
        # We only parse media if it is not already parsed
        if self.media.is_parsed() == 0:
            self.media.parse()

        # We return the meta data for the given tag
        # We use getattr() to call a specific attribute based on the given string
        # The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
        try:
            return f"{tag}: {self.media.get_meta(getattr(Meta, tag))}"
        except TypeError:
            # We raise TypeError if the the argument is not a string
            raise TypeError("The argument be must a string.")
        except AttributeError:
            # We raise AttributeError if the given tag is not valid
            raise AttributeError(
                "No meta data found for the given tag. Check the documentation for the list of valid tags.")

    def edit_meta(self, tag: str, value: str) -> str:  # defining the edit function
        # We need to first parse media to get meta data
        # We only parse media if it is not already parsed
        if self.media.is_parsed() == 0:
            self.media.parse()

        # We set the meta data for the given tag to the given value
        # We use getattr() to call a specific attribute based on the given string
        # The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
        try:
            self.media.set_meta(getattr(Meta, tag), value)
            self.media.save_meta()
            return f"Changed {tag} to {value}"
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a string.")
        except TypeError:
            # We raise TypeError if the the argument is not a string
            raise TypeError("The argument must be a string.")
        except AttributeError:
            # We raise AttributeError if the given tag is not valid
            raise AttributeError(
                "No meta data found for the given tag. Check documentation for the list of valid tags.")

        # Supported Tags:
        # Actors = vlc.Meta.Actors
        # Album = vlc.Meta.Album
        # AlbumArtist = vlc.Meta.AlbumArtist
        # Artist = vlc.Meta.Artist
        # ArtworkURL = vlc.Meta.ArtworkURL
        # Copyright = vlc.Meta.Copyright
        # Date = vlc.Meta.Date
        # Description = vlc.Meta.Description
        # Director = vlc.Meta.Director
        # DiscNumber = vlc.Meta.DiscNumber
        # DiscTotal = vlc.Meta.DiscTotal
        # EncodedBy = vlc.Meta.EncodedBy
        # Episode = vlc.Meta.Episode
        # Genre = vlc.Meta.Genre
        # Language = vlc.Meta.Language
        # NowPlaying = vlc.Meta.NowPlaying
        # Publisher = vlc.Meta.Publisher
        # Rating = vlc.Meta.Rating
        # Season = vlc.Meta.Season
        # Setting = vlc.Meta.Setting
        # ShowName = vlc.Meta.ShowName
        # Title = vlc.Meta.Title
        # TrackID = vlc.Meta.TrackID
        # TrackNumber = vlc.Meta.TrackNumber
        # TrackTotal = vlc.Meta.TrackTotal
        # URL = vlc.Meta.URL


    def start(self) -> str:  # defining the start function
        self.player.play()
        return f"Now playing {self.meta('Title')}"

    def pause(self, status: bool) -> str:  # defining the pause function
        # We pause/resume the playback based the the argument
        try:
            self.player.set_pause(status)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a boolean.")

        return f"{'Paused' if status else 'Resumed'}"

    def mute(self, status: bool) -> str:  # defining the mute function
        # We mute/unmute the playback based the the argument
        try:
            self.player.audio_Set_mute(status)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a boolean.")

        return f"{'Muted' if status else 'Unmuted'}"

    def set_volume(self, vol: int = 100) -> str:  # defining the set_volume function
        try:
            self.player.audio_set_volume(vol)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a int.")

        return f"Volume set to {vol}%"

    def stop(self) -> None:  # defining the stop function
        self.player.stop()

        # This is required otherwise playing again after calling stop() boosts volume
        self.__init__(self.file_path)
