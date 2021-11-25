import sys
import os
import pygame

from player import Player
from gui import GUI

for root, dirs, files in os.walk("music"):
    for filename in files:
        print(filename[-4:])

DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = DIR + "\music\\"
PIXS_DIR = DIR + "\pixs\\"

WIDTH = 1000
HEIGHT = 600

running = True
gui = GUI(WIDTH, HEIGHT)
player = Player(MUSIC_DIR)
player.load_track('Vitality.mp3')

if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.playing:
                        player.change_pause()
                    else:
                        player.play_track()

                if event.key == pygame.K_UP:
                    player.change_volume(0.05)
                elif event.key == pygame.K_DOWN:
                    player.change_volume(-0.05)

                if event.key == pygame.K_m:
                    player.change_mute()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    player.change_volume(0.015)

                elif event.button == 5:
                    player.change_volume(-0.015)

        gui.screen_update()
