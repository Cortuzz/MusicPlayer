import pygame
from mutagen.mp3 import MP3


class Player:
    def __init__(self, dir, songs):
        self.dir = dir
        self.songs = songs
        self.current_song_index = 0

        self.volume = 0.2
        self.playing = False
        self.paused = False
        self.muted = False
        self.length = 0
        self.time = 0

        self.change_volume()

    def load_track(self, name):
        pygame.mixer.music.load(self.dir + name)
        audio = MP3(self.dir + name)

        self.length = audio.info.length

    def change_pause(self):
        if self.playing:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True
        else:
            self.load_track(self.songs[self.current_song_index])

            pygame.mixer.music.play()
            self.playing = True
            self.paused = False

    def next_track(self):
        self.current_song_index += 1

        if self.current_song_index >= len(self.songs):
            self.current_song_index = 0

        self.change_track()

    def prev_track(self):
        self.current_song_index -= 1

        if self.current_song_index < 0:
            self.current_song_index = len(self.songs) - 1

        self.change_track()

    def change_track(self):
        self.load_track(self.songs[self.current_song_index])

        if self.playing and not self.paused:
            pygame.mixer.music.play()

        if self.playing and self.paused:
            self.playing = False

        self.time = 0

    def change_volume(self, difference=0, is_percentage=False):
        if is_percentage:
            self.volume = difference
        else:
            self.volume = min(max(self.volume + difference, 0), 1)

        pygame.mixer.music.set_volume(self.volume)

    def change_mute(self):
        if self.muted:
            pygame.mixer.music.set_volume(self.volume)
            self.muted = False
        else:
            pygame.mixer.music.set_volume(0)
            self.muted = True

    def change_position(self, difference, is_percentage=False):
        current_position = self.get_duration()['current_time']
        self.time = current_position + difference * 1000

        if is_percentage:
            self.time = 1000 * difference * self.length

        if self.time < 0:
            self.time = 0

        pygame.mixer.music.play(0, self.time // 1000)

        if self.paused:
            pygame.mixer.music.pause()

        if self.time > 1000 * self.length:
            self.next_track()

    def check_end(self):
        if not pygame.mixer.music.get_busy() and not self.paused and self.playing:
            self.next_track()

    def get_duration(self):
        return {'current_time': self.time + pygame.mixer.music.get_pos(),
        'total_time': self.length}

    def get_volume(self):
        return self.volume, self.muted

    def get_songs(self):
        return self.songs, self.current_song_index
