import sys
import os
import ctypes
import pygame

from button import *
from player import Player
from gui import GUI


songs = []
for root, dirs, files in os.walk("music"):
    for filename in files:
        if filename[-4:] == '.mp3':
            songs.append(filename)

if not len(songs):
    ctypes.windll.user32.MessageBoxW(
    None, u"Folder music must contain at least 1 mp3 file", u"Error", 0)
    exit()

DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = DIR + "\music\\"
PIXS_DIR = DIR + "\pixs\\"

WIDTH = 1000
HEIGHT = 600

running = True

pause_button = Pause((566, 450), 200, 75)
next_button = NextTrack((833, 450), 75, 75)
prev_button = PrevTrack((424, 450), 75, 75)

buttons = pause_button, next_button, prev_button

gui = GUI(WIDTH, HEIGHT, buttons)
player = Player(MUSIC_DIR, songs)

if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.change_pause()

                if event.key == pygame.K_UP:
                    player.change_volume(0.05)
                elif event.key == pygame.K_DOWN:
                    player.change_volume(-0.05)

                if event.key == pygame.K_m:
                    player.change_mute()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        button.try_action(event.pos, player)
                if event.button == 4:
                    player.change_volume(0.015)

                elif event.button == 5:
                    player.change_volume(-0.015)

        gui.screen_update()
