import pygame
from os import path

class ImageDrawer:
    def __init__(self, player):
        pass

    def load_image(self, song_name):
        if not path.isfile('./images' + song_name + '.jpg'):
                '''TODO :
                create blank square file
                with name song_name.jpg in images folder
                '''
        image = pygame.image.load('./images' + song_name + '.jpg')
        return image
