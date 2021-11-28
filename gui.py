import pygame
from button import RectButton, CircleButton


class GUI:
    def __init__(self, width, height, buttons):
        self.width = width
        self.height = height
        self.buttons = buttons

        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, (self.width + self.height) // 50)
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

    def convert_to_time(self, time):
        if time < 0:
            time = 0

        minutes = str(int(time // 60)).zfill(2)
        seconds = str(int(time % 60)).zfill(2)

        return minutes, seconds

    def render_duration(self, time, total_time):
        time //= 1000
        minutes, seconds = self.convert_to_time(time)
        time = self.font.render(
        "{}:{}".format(minutes, seconds), False, (14, 18, 49))

        minutes, seconds = self.convert_to_time(total_time)
        total_time = self.font.render(
        "{}:{}".format(minutes, seconds), False, (14, 18, 49))

        self.screen.blit(time, (1.25 * self.width // 3, 2.1 * self.height // 3))

        self.screen.blit(total_time, (2.6 * self.width // 3, 2.1 * self.height // 3))

    def render_buttons(self):
        for button in self.buttons:
            coordinates = button.get_coordinates()

            if isinstance(button, RectButton):
                rectangle_button = pygame.Rect(
                coordinates['x'], coordinates['y'],
                coordinates['width'], coordinates['height'])

                pygame.draw.rect(self.screen, (55, 55, 91), rectangle_button)

            if isinstance(button, CircleButton):
                pygame.draw.circle(self.screen, (55, 55, 91),
                (coordinates['x'], coordinates['y']), coordinates['radius'])

    def render_track_image(self, image_name, x, y):
        surface=pygame.image.load(image_name)
        surface = pygame.transform.scale(surface, (self.width // 3, self.width // 3))
        image_rect=surface.get_rect(topleft=(x, y))
        self.screen.blit(surface,image_rect)

    def screen_update(self, time, total_time, image_name):
        self.render_track_image(
        'images/{}'.format(image_name), self.width // 2, self.height // 12)

        self.render_borders()
        self.render_buttons()
        self.render_duration(time, total_time)
        pygame.display.update()
        self.screen.fill((98, 97, 136))
