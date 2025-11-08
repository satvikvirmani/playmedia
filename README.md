<p align="center">
    <h1 align="center">playmedia</h1>
</p>

<p align="center">
    <strong>A powerful Python module to play and control media files with ease</strong>
</p>

<p align="center">
    <a href="https://github.com/satvikvirmani/playmedia">
        <img src="https://img.shields.io/badge/Made%20by%20Satvik%20Virmani-000000?style=for-the-badge">
    </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
  <img src="https://img.shields.io/github/issues/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/satvikvirmani/playmedia?color=000000&logoColor=000000&style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.0%2B-blue?style=for-the-badge">
</p>

---

## Features

- **Single File Playback** - Play individual audio/video files with full control
- **Playlist Management** - Handle multiple files as a playlist with navigation
- **Complete Control** - Play, pause, stop, volume control, and mute functionality
- **Metadata Support** - Read and edit 26+ metadata tags
- **Multi-Format** - Supports 8 major audio and video formats
- **Pythonic API** - Clean, intuitive interface with helpful return messages
- **VLC Powered** - Built on robust VLC media player backend

---

## Installation

```bash
pip install playmedia
```

### Dependencies

**Required:** [VLC Media Player](https://sourceforge.net/projects/vlc/)

Make sure VLC is installed on your system before using playmedia.

**Python Packages** (automatically installed):
- `python-vlc` - VLC Python bindings
- `pretty-errors` - Enhanced error formatting

---

## Quick Start

### Single File Playback

```python
from playmedia import File

# Create a player instance
player = File("path/to/song.mp3")

# Start playback
print(player.start())  # Output: Now playing Song Title

# Control playback
print(player.pause(True))  # Output: Paused
print(player.pause(False))  # Output: Resumed
print(player.set_volume(75))  # Output: Volume set to 75%
print(player.mute(True))  # Output: Muted

# View metadata
print(player.meta("Artist"))  # Output: Artist: Artist Name
print(player.meta("Album"))  # Output: Album: Album Name

# Edit metadata
print(player.edit_meta("Album", "My Custom Album"))

# Stop playback
player.stop()
```

### Playlist Management

```python
from playmedia import Files

# From a directory
playlist = Files("path/to/music/folder")

# Or from a list of files
playlist = Files([
    "song1.mp3",
    "song2.mp3",
    "song3.flac"
])

# View available files
print(playlist.get_list())
# Output: {0: 'Song 1.mp3', 1: 'Song 2.mp3', 2: 'Song 3.flac'}

# Start playing from beginning
playlist.start()

# Navigate through playlist
print(playlist.next())  # Output: Now playing Song 2
print(playlist.previous())  # Output: Now playing Song 1

# Jump to specific track
print(playlist.play_at_index(2))  # Output: Now playing Song 3

# Control playback
playlist.pause(True)
playlist.set_volume(80)
playlist.mute(False)

# Get current track info
print(playlist.current_meta("Title"))
print(playlist.current_time())  # Output: {'Current time': '45.32s'}

# Stop playlist
playlist.stop()
```

---

## API Reference

### File Class

**`File(path: str)`**

Initialize a single file player.

#### Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `start()` | None | `str` | Starts playback |
| `pause(status)` | `status: bool` | `str` | Pauses (True) or resumes (False) |
| `mute(status)` | `status: bool` | `str` | Mutes (True) or unmutes (False) |
| `set_volume(vol)` | `vol: int` (0-100) | `str` | Sets volume level |
| `meta(tag)` | `tag: str` | `str` | Retrieves metadata |
| `edit_meta(tag, value)` | `tag: str, value: str` | `str` | Edits metadata |
| `stop()` | None | `None` | Stops playback |

### Files Class

**`Files(arg: str | list)`**

Initialize a playlist from directory path or list of file paths.

#### Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `get_list()` | None | `dict` | Returns indexed file dictionary |
| `start()` | None | `dict` | Starts sequential playback |
| `play_at_index(index)` | `index: int` | `str` | Plays file at index |
| `pause(status)` | `status: bool` | `str` | Pauses or resumes |
| `next()` | None | `str` | Skips to next track |
| `previous()` | None | `str` | Returns to previous track |
| `mute(status)` | `status: bool` | `str` | Mutes or unmutes |
| `set_volume(vol)` | `vol: int` (0-100) | `str` | Sets volume level |
| `current_meta(tag)` | `tag: str` | `str` | Gets current track metadata |
| `current_time()` | None | `dict` | Gets current playback time |
| `stop()` | None | `None` | Stops playlist |

---

## Supported Metadata Tags

Both classes support the following metadata tags:

`Actors`, `Album`, `AlbumArtist`, `Artist`, `ArtworkURL`, `Copyright`, `Date`, `Description`, `Director`, `DiscNumber`, `DiscTotal`, `EncodedBy`, `Episode`, `Genre`, `Language`, `NowPlaying`, `Publisher`, `Rating`, `Season`, `Setting`, `ShowName`, `Title`, `TrackID`, `TrackNumber`, `TrackTotal`, `URL`

---

## Supported File Formats

- **Audio:** `.m4a`, `.flac`, `.mp3`, `.wav`, `.wma`, `.aac`
- **Video:** `.mp4`, `.mkv`

---

## Usage Tips

### Return Values

All control methods return descriptive strings that can be printed for user feedback:

```python
player = File("song.mp3")
message = player.start()
print(message)  # "Now playing Song Title"
```

### Error Handling

The module provides clear error messages for common issues:

```python
try:
    player = File("nonexistent.mp3")
except FileNotFoundError as e:
    print(e)  # "No file found for the given path."

try:
    player.pause("invalid")
except TypeError as e:
    print(e)  # "The argument must be a boolean."
```

### Metadata Access

Always ensure a file is playing before accessing `current_meta()` in the Files class:

```python
playlist = Files("music/")
playlist.start()  # Start playback first
print(playlist.current_meta("Artist"))  # Now safe to access
```

---

## Use Cases

- **Music Players:** Build custom music player applications
- **Media Management:** Organize and play media libraries
- **Automation:** Script media playback for events or scheduling
- **Audio Processing:** Integrate playback into audio analysis workflows
- **Educational Tools:** Create interactive media learning applications
- **Background Music:** Add soundtrack capabilities to applications

---

## Known Issues & Notes

- After calling `stop()`, the player reinitializes to prevent volume boost bugs
- `current_meta()` requires active playback - call `start()` or `play_at_index()` first
- VLC Media Player must be installed system-wide

---

## Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/satvikvirmani/playmedia/issues).

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Author

### **Satvik Virmani**

<a href="https://twitter.com/satvikvirmani">
    <img src="https://img.shields.io/twitter/follow/satvikvirmani?color=000000&logo=twitter&logoColor=FFFFFF&style=for-the-badge">
</a>

- **Email:** virmanisatvik01@gmail.com
- **GitHub:** [@satvikvirmani](https://github.com/satvikvirmani)

---

## Show Your Support

Give a ⭐️ if this project helped you!

Your support motivates continued development and improvement.

---

## Acknowledgments

- Built with [python-vlc](https://github.com/oaubert/python-vlc)
- Powered by [VLC Media Player](https://www.videolan.org/vlc/)
- Enhanced errors by [pretty-errors](https://github.com/onelivesleft/PrettyErrors)

---

<p align="center">
    Made with ❤️ by Satvik Virmani
</p>
