import sql
import sys
import pygame

from gui import GUI


running = True
WIDTH = 600
HEIGHT = 800
gui = GUI(WIDTH, HEIGHT)

if __name__ == '__main__':
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		gui.screen_update()
