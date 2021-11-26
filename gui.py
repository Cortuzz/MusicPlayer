import pygame
from button import Button


class GUI:
    def __init__(self, width, height, buttons):
        self.width = width
        self.height = height
        self.buttons = buttons

        pygame.init()
        pygame.display.set_caption("Music Player")
        self.screen = pygame.display.set_mode((width, height))

    def render_borders(self):
        # playlist part rendering
        playlist_part = 3
        vertical_playlist_part = 6

        pygame.draw.line(self.screen, (255, 255, 255),
        [self.width // playlist_part, 0],
        [self.width // playlist_part, self.height], 4)

        for i in range(1, self.height // vertical_playlist_part):
            pygame.draw.line(self.screen, (255, 255, 255),
            [0, i * self.height // vertical_playlist_part],
            [self.width // playlist_part, i * self.height // vertical_playlist_part], 2)

    def render_playlist(self):
        pass

    def render_volume(self):
        pass

    def render_duration(self):
        pass

    def render_buttons(self):
        for button in self.buttons:
            coordinates = button.get_coordinates()

            rectangle_button = pygame.Rect(
            coordinates['x'], coordinates['y'],
            coordinates['width'], coordinates['height'])

            pygame.draw.rect(self.screen, (120, 78, 175), rectangle_button)

    def render_track_image(self):
        pass  # TODO

    def screen_update(self):
        self.render_borders()
        self.render_buttons()
        pygame.display.update()
        self.screen.fill((0, 0, 0))
