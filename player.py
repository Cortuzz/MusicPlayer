import pygame


class Player:
    def __init__(self, dir):
        self.dir = dir
        self.volume = 0.2
        self.playing = False
        self.muted = False

    def load_track(self, name):
        pygame.mixer.music.load(self.dir + name)

    def play_track(self):
        pygame.mixer.music.play()

    def change_volume(self, difference):
        self.volume =min(max(self.volume + difference, 0), 1)
        pygame.mixer.music.set_volume(self.volume)


    def change_mute(self):
        if self.muted:
            pygame.mixer.music.set_volume(self.volume)
            return

        pygame.mixer.music.set_volume(0)
