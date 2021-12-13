import sys
import os
import ctypes
import pygame

from button import *
from player import Player
from gui import GUI
from handler import Handler


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

pause_button = \
    Pause((WIDTH * 2 // 3, HEIGHT * 2.5 // 3), (WIDTH + HEIGHT) // 32)

next_button = NextTrack(
        (
            WIDTH * 2 // 3 + 3 * (WIDTH + HEIGHT) // 64 + WIDTH // 100,
            HEIGHT * 2.5 // 3
        ),
        (WIDTH + HEIGHT) // 64)

prev_button = PrevTrack(
        (
            WIDTH * 2 // 3 - 3 * (WIDTH + HEIGHT) // 64 - WIDTH // 100,
            HEIGHT * 2.5 // 3
        ),
        (WIDTH + HEIGHT) // 64)

duration_bar = DurationBar(
    (1.45 * WIDTH // 3, 2.14 * HEIGHT // 3 - 1),
    1.10 * WIDTH // 3, 6, (255, 255, 255))

volume_bar = VolumeBar(
    (WIDTH // 1.1 - 4, HEIGHT // 10),
    8, HEIGHT // 1.6 - HEIGHT // 10, (255, 255, 255))

buttons = [pause_button, next_button, prev_button, duration_bar, volume_bar]

gui = GUI(WIDTH, HEIGHT, buttons)
player = Player(MUSIC_DIR, songs)
handler = Handler(player, buttons)

if __name__ == '__main__':
    player.load_track(songs[0])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                handler.keyboard_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handler.mouse_events(event)

        player.check_end()
        time = player.get_duration()
        gui.screen_update(time['current_time'], time['total_time'],
        'Vitality.jpg', player.get_volume(), player.get_songs()[0],
        player.get_songs()[1])
