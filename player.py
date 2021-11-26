import pygame


class Player:
    def __init__(self, dir, songs):
        self.dir = dir
        self.songs = songs
        self.current_song_index = 0

        self.volume = 0.2
        self.playing = False
        self.paused = False
        self.muted = False

    def load_track(self, name):
        pygame.mixer.music.load(self.dir + name)

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

    def change_volume(self, difference):
        self.volume = min(max(self.volume + difference, 0), 1)
        pygame.mixer.music.set_volume(self.volume)

    def change_mute(self):
        if self.muted:
            pygame.mixer.music.set_volume(self.volume)
            self.muted = False
        else:
            pygame.mixer.music.set_volume(0)
            self.muted = True

    def get_duration(self):
        return pygame.mixer.music.get_pos()
