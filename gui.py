import pygame


class GUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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

    def screen_update(self):
        self.render_borders()

        pygame.display.update()
        self.screen.fill((0, 0, 0))
