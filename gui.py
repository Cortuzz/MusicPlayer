import pygame
from button import Button


class GUI:
    def __init__(self, width, height, pause_button):
        self.width = width
        self.height = height
        self.pause_button=pause_button
        pygame.init()
        pygame.display.set_caption("Music Player")
        self.screen = pygame.display.set_mode((width, height))

    def render_borders(self):
        pygame.draw.line(self.screen, (255, 255, 255),
        [self.width // 3, 0], [self.width // 3, self.height], 4)

        for i in range(1, self.height // 6):
            pygame.draw.line(self.screen, (255, 255, 255),
            [0, i * self.height // 6], [self.width // 3, i * self.height // 6], 2)

    def render_playlist(self):
        pass

    def render_volume(self):
        pass

    def render_duration(self):
        pass

    def render_button(self):
        rectangle_button = pygame.Rect(
        self.pause_button.x, self.pause_button.y,
        self.pause_button.width, self.pause_button.height)
        pygame.draw.rect(self.screen, (120, 78, 175), rectangle_button)

    def render_track_image(self):
        pass #TODO

    def screen_update(self):
        self.render_borders()
        self.render_button()
        pygame.display.update()
        self.screen.fill((0, 0, 0))
