import pygame


class GUI:
	def __init__(self, width, height):
		pygame.font.init()
		pygame.init()
		pygame.display.set_caption("Music Player")
		self.screen = pygame.display.set_mode((width, height))

	def screen_update(self):
		pygame.display.update()
		self.screen.fill((0, 0, 0))
