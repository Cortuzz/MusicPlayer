class Button:
    def __init__(self):
        pass

    def action(self, player):
        pass

    def collision(self, x, y):
        pass

    def try_action(self, mouse_coords, player):
        mouse_x, mouse_y = mouse_coords
        if self.collision(mouse_x, mouse_y):
                self.action(player)

    def get_coordinates(self):
        pass

    def get_color(self):
        return self.color


class RectButton(Button):
    def __init__(self, left_top_coordinates, width, height, color=(55, 55, 91)):
        self.x, self.y = left_top_coordinates
        self.width = width
        self.height = height
        self.color = color

    def collision(self, x, y):
        return \
            self.x <= x <= self.x + self.width and \
            self.y <= y <= self.y + self.height

    def get_coordinates(self):
        return {'x': self.x, 'y': self.y,
        'width': self.width, 'height': self.height}


class CircleButton(Button):
    def __init__(self, center_coordinates, radius, color=(55, 55, 91)):
        self.x, self.y = center_coordinates
        self.radius = radius
        self.color = color

    def collision(self, x, y):
        return (x - self.x)**2 + (y - self.y)**2 <= self.radius**2

    def get_coordinates(self):
        return {'x': self.x, 'y': self.y,
        'radius': self.radius}


class Pause(CircleButton):
    def action(self, player):
        player.change_pause()


class NextTrack(CircleButton):
    def action(self, player):
        player.next_track()


class PrevTrack(CircleButton):
    def action(self, player):
        player.prev_track()


class DurationBar(RectButton):
    def action(self, player, track_percentage):
        player.change_position(track_percentage, True)

    def try_action(self, mouse_coords, player):
        mouse_x, mouse_y = mouse_coords
        track_percentage = (mouse_x - self.x) / self.width

        if self.collision(mouse_x, mouse_y):
                self.action(player, track_percentage)


class VolumeBar(RectButton):
    def action(self, player, percentage):
        player.change_volume(percentage, True)

    def try_action(self, mouse_coords, player):
        mouse_x, mouse_y = mouse_coords
        percentage = 1 - (mouse_y - self.y) / self.height

        if self.collision(mouse_x, mouse_y):
                self.action(player, percentage)
