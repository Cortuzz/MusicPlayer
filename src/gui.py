import pygame
from button import RectButton, CircleButton


class GUI:
    def __init__(self, width, height, buttons):
        self.width = width
        self.height = height
        self.buttons = buttons

        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.font.init()

        self.font = pygame.font.Font(None, (self.width + self.height) // 50)
        pygame.display.set_caption("Music Player")
        self.screen = pygame.display.set_mode((width, height))

    def render_playlist(self, tracks, current_track_index):
        playlist_part = 3
        vertical_playlist_part = 6

        pygame.draw.line(self.screen, (255, 255, 255),
        [self.width // playlist_part, 0],
        [self.width // playlist_part, self.height], 4)

        for i in range(1, self.height // vertical_playlist_part):
            pygame.draw.line(self.screen, (255, 255, 255),
            [0, i * self.height // vertical_playlist_part],
            [self.width // playlist_part, i * self.height // vertical_playlist_part], 2)

        for i in range(current_track_index, len(tracks)):
            song_name = self.font.render(tracks[i].split('.mp3')[0], False,
            (14, 18, 100) if i == current_track_index else (14, 18, 49))

            self.screen.blit(song_name,
            (0.1 * self.width / playlist_part,
            (i - current_track_index) * self.height // vertical_playlist_part +
            self.height // vertical_playlist_part // 2 - 8))

        for i in range(current_track_index):
            song_name = self.font.render(
            tracks[i].split('.mp3')[0], False, (14, 18, 49))

            self.screen.blit(song_name,
            (0.1 * self.width / playlist_part,
            (i + len(tracks) - current_track_index) * self.height //
            vertical_playlist_part + self.height // vertical_playlist_part // 2 - 8))

    def convert_to_time(self, time):
        if time < 0:
            time = 0

        minutes = str(int(time // 60)).zfill(2)
        seconds = str(int(time % 60)).zfill(2)

        return minutes, seconds

    def render_time(self, time, total_time):
        time //= 1000
        minutes, seconds = self.convert_to_time(time)
        time = self.font.render(
        "{}:{}".format(minutes, seconds), False, (14, 18, 49))

        minutes, seconds = self.convert_to_time(total_time)
        total_time = self.font.render(
        "{}:{}".format(minutes, seconds), False, (14, 18, 49))

        self.screen.blit(time, (1.25 * self.width // 3, 2.1 * self.height // 3))

        self.screen.blit(total_time, (2.6 * self.width // 3, 2.1 * self.height // 3))

    def render_duration_border(self):
        pygame.draw.circle(self.screen, (255, 255, 255),
        (1.45 * self.width // 3, 2.15 * self.height // 3), 4)

        pygame.draw.line(self.screen, (255, 255, 255),
        [1.45 * self.width // 3, 2.15 * self.height // 3 - 1],
        [2.55 * self.width // 3, 2.15 * self.height // 3 - 1], 8)

        pygame.draw.circle(self.screen, (255, 255, 255),
        (2.55 * self.width // 3, 2.15 * self.height // 3), 4)

    def render_duration(self, time, total_time):
        percentage = time / total_time / 1000
        coordinate = percentage * (1.1 * self.width // 3) + 1.45 * self.width // 3

        pygame.draw.circle(self.screen, (55, 55, 91),
        (1.45 * self.width // 3, 2.15 * self.height // 3), 3)

        # active part
        pygame.draw.line(self.screen,(55, 55, 91),
        [1.45 * self.width // 3, 2.15 * self.height // 3 - 1],
        [coordinate, 2.15 * self.height // 3 - 1], 6)

        pygame.draw.circle(self.screen, (55, 55, 91),
        (coordinate, 2.15 * self.height // 3), 5)

    def render_volume_border(self):
        pygame.draw.circle(self.screen, (255, 255, 255),
        (self.width // 1.1, self.height // 10), 4)

        pygame.draw.line(self.screen, (255, 255, 255),
        [self.width // 1.1 - 1, self.height // 10],
        [self.width // 1.1 - 1, self.height // 1.6], 8)

        pygame.draw.circle(self.screen, (255, 255, 255),
        (self.width // 1.1, self.height // 1.6), 4)

    def render_volume(self, volume, is_muted=False):
        volume_position = self.height // 1.6 - \
        volume * (self.height // 1.6 - self.height // 10)

        color = (volume * 255, 55, 91)
        if is_muted:
            color = (128, 128, 128)

        pygame.draw.circle(self.screen, color,
        (self.width // 1.1, volume_position), 5)

        pygame.draw.line(self.screen, color,
        [self.width // 1.1 - 1, volume_position],
        [self.width // 1.1 - 1, self.height // 1.6], 6)

        pygame.draw.circle(self.screen, color,
        (self.width // 1.1, self.height // 1.6), 3)

    def render_buttons(self):
        for button in self.buttons:
            coordinates = button.get_coordinates()
            color = button.get_color()

            if isinstance(button, RectButton):
                rectangle_button = pygame.Rect(
                coordinates['x'], coordinates['y'],
                coordinates['width'], coordinates['height'])

                pygame.draw.rect(self.screen, color, rectangle_button)

            if isinstance(button, CircleButton):
                pygame.draw.circle(self.screen, color,
                (coordinates['x'], coordinates['y']), coordinates['radius'])

    def render_track_image(self, image_name, x, y):
        surface = pygame.image.load(image_name)
        surface = pygame.transform.scale(surface, (self.width // 3, self.width // 3))
        image_rect = surface.get_rect(topleft = (x, y))
        self.screen.blit(surface, image_rect)

    def screen_update(self, time, total_time, image_name, volume_stat, tracks, index):
        self.render_track_image(
        'images/{}'.format(image_name), self.width // 2, self.height // 12)

        self.render_time(time, total_time)
        self.render_buttons()
        self.render_duration_border()
        self.render_duration(time, total_time)
        self.render_volume_border()
        self.render_volume(volume_stat[0], volume_stat[1])
        self.render_playlist(tracks, index)

        pygame.display.update()
        self.screen.fill((98, 97, 136))

        self.clock.tick(15)
