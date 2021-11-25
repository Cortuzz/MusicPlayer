import pygame


class Player:
    def __init__(self, dir):
        self.dir = dir
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
            pygame.mixer.music.play()
            self.playing = True

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
