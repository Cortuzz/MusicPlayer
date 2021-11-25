import sys
import os
import pygame

from player import Player
from gui import GUI

for root, dirs, files in os.walk("music"):
    for filename in files:
        print(filename[-4:])


DIR = os.path.dirname(os.path.abspath(__file__)) + "\music\\"
WIDTH = 800
HEIGHT = 500

running = True
gui = GUI(WIDTH, HEIGHT)
player = Player(DIR)
player.load_track('Vitality.mp3')

if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player.playing:
                    player.playing = True
                    player.play_track()
                if event.key == pygame.K_UP:
                    player.change_volume(0.05)
                if event.key == pygame.K_DOWN:
                    player.change_volume(-0.05)
                if event.key == pygame.K_m:
                    player.change_mute()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    player.change_volume(0.015)

                elif event.button == 5:
                    player.change_volume(-0.015)

        gui.screen_update()
