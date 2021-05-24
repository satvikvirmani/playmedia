from threading import Thread
import vlc, os, random, time

stopped_multiple = False
stopped_single = False
single_instance = None
multiple_instance = None

class SinglePlayer:
    def __init__(self, file):
        self.player = vlc.MediaPlayer()
        self.player.audio_set_volume(100)
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
    def __init__(self, path, shuffle):
        self.player = vlc.MediaListPlayer()
        self.list = vlc.MediaList()
        self.player.get_media_player().audio_set_volume(100)
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

def play_flow_multiple(path, shuffle):
    global multiple_instance
    multiple_instance = MultiplePlayer(path, shuffle)
    multiple_instance.start_playing()
    global stopped_multiple
    while True:
        if stopped_multiple:
            break
def play_multiple(path,shuffle=False):
    thread_a = Thread(target=play_flow_multiple, args=(path,shuffle))
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

def play_flow_single(url, bugFix):
    global single_instance
    single_instance = SinglePlayer(url)
    single_instance.start_playing()
    global stopped_single
    while True:
        if stopped_single:
            break
def play_single(url, bugFix=False):
    thread_b = Thread(target=play_flow_single, args=(url, bugFix))
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