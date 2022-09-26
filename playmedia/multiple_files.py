from ctypes import ArgumentError
from typing import Union

# importing the classes from python-vlc
from vlc import Media, MediaList, MediaListPlayer, Meta

# importing Path class from pathlib
from pathlib import Path

# importing pretty-errors module (This module is not accessed but importing it formats the errors raised and display them nicely in the terminal)
import pretty_errors


class Files:

    def __init__(self, arg: Union[str, list]) -> None:  # defining the init function
        # initially setting files variable equal to empty list
        self.files = []
        # initially setting path variable equal to ""
        self.path = ""

        if type(arg) == list:
            self.files = arg
        elif (type(arg) == str):
            self.path = arg
        else:
            raise RuntimeError("The argument can either be a list or string.")

        # setting list_player variable equal to the MediaListPlayer Class of python-vlc
        self.list_player = MediaListPlayer()
        # setting player variable equal to the MediaPlayer instance of the self.list_player
        self.player = self.list_player.get_media_player()

        # Resetting all settings
        self.player.audio_set_volume(100)
        self.list_player.set_pause(False)
        self.player.audio_set_mute(False)

        self.set_list()  # We call the set_list method initially

    def set_list(self) -> None:  # defining the set_list function
        # setting list variable equal to the MediaList Class of python-vlc
        self.list = MediaList()

        # Types of media files supported by libvlc
        supported_files = ['.m4a', '.flac', '.mp3',
                           '.mp4', '.wav', '.wma', '.aac', '.mkv']

        if self.files == [] and self.path != "":
            # Check if the path exists
            if Path(self.path).exists():
                for path in Path(self.path).iterdir():

                    # Add file only if the file is supported
                    if path.suffix in supported_files:
                        self.media = Media(str(path))
                        # Adding media the the list
                        self.list.add_media(self.media)
            else:
                # If the given path does not exist then we raise FileNotFoundError
                raise FileNotFoundError(
                    f"The given path \"{self.path}\" does not exist.")

        elif self.files != [] and self.path == "":

            for path in self.files:
                # Add file only if the file is supported
                if Path(path).suffix in supported_files:
                    self.media = Media(str(path))
                    # Adding media the the list
                    self.list.add_media(self.media)
                else:
                    if Path(path).suffix == "":
                        # If the file is not valid then we raise FileNotFoundError
                        raise RuntimeError(
                            f"The given directory does not contain any supported media file.")
                    else:
                        # If the file is not valid then we raise FileNotFoundError
                        raise FileNotFoundError(
                            f"The extension \"{Path(path).suffix}\" not supported. Check the documentation for the list of valid media files.")
        else:
            # If the arguments are invalid then we raise RuntimeError
            raise RuntimeError("The argument is invalid.")

        i = 0
        self.file_dict = {}
        while i < self.list.count():
            item = self.list.item_at_index(i)
            item.parse()
            self.file_dict[i] = item.get_meta(Meta.Title)
            i = i + 1
        # Setting the list in the list_player
        self.list_player.set_media_list(self.list)

    def get_list(self) -> dict:  # defining the get_list function
        return self.file_dict

    def start(self) -> dict:  # defining the start function
        self.list_player.play()
        return self.file_dict

    def play_at_index(self, index: int) -> str:  # defining the play_at_index function
        try:
            self.list_player.play_item_at_index(index)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a boolean.")

        return f"Now playing {self.current_meta('Title')}"

    def pause(self, status: bool) -> str:  # defining the pause function
        # We pause/resume the playback based the the argument
        try:
            self.list_player.set_pause(status)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a boolean.")

        return f"{'Paused' if status else 'Resumed'}"

    def next(self) -> str:  # defining the next function
        self.list_player.next()
        return f"Now playing {self.current_meta('Title')}"

    def previous(self) -> str:  # defining the previous function
        self.list_player.previous()
        return f"Now playing {self.current_meta('Title')}"

    def set_volume(self, vol: int = 100) -> str:  # defining the set_volume function
        try:
            self.player.audio_set_volume(vol)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a int.")

        return f"Volume set to {vol}%"

    def mute(self, status: bool) -> str:  # defining the mute function
        # We mute/unmute the playback based the the argument
        try:
            self.player.audio_Set_mute(status)
        except ArgumentError:  # python-vlc throws the ctypes.ArgumentError, We handle that error and then throw a TypeError
            raise TypeError("The argument must be a boolean.")

        return f"{'Muted' if status else 'Unmuted'}"

    def stop(self) -> str:  # defining the set_volume function
        self.list_player.stop()

        # This is required otherwise playing again after calling stop() boosts volume
        self.__init__(self.path)

    # should be invoked only when a media is playing
    def current_meta(self, tag: str = "Date") -> str:  # defining the current_meta function
        current_media = self.player.get_media()

        if current_media == None:
            raise IndexError("No media found for this given index.")
        else:
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

    def current_time(self) -> dict:  # defining the current_time function
        return {
            "Current time": f"{round(self.player.get_time()/1000, 2)}s"
        }