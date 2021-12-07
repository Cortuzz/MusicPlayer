class Button:
    def __init__(self):
        '''
        1st input is tuple with pair of coordinates
        2st and 3d inputs are corresponding width and height
        '''
        pass

        # self.exception_handler()  # DOES NOT WORK!!!

    def exception_handler():  # TODO DA. YES.
        if not(isinstance(
                self.left_top, tuple) and
                isinstance(self.right_bottom, tuple)
            ):
            raise TypeError(
            "Object Button takes 2 tuples but {} and {} were given".format(
            type(self.left_top), type(self.right_bottom)))

        if not (len(self.left_top) == 2 and len(self.right_bottom) == 2):
            raise ValueError(
            "Tuples left_top and right_bottom contains 2 coordinates \
            but {} and {} were given".format(
            len(self.left_top), len(self.right_bottom)))

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


class RectButton(Button): # TODO: center coordinates
    def __init__(self, left_top_coordinates, width, height):
        self.x, self.y = left_top_coordinates
        self.width = width
        self.height = height # create color

    def collision(self, x, y):
        return \
            self.x <= x <= self.x + self.width and \
            self.y <= y <= self.y + self.height

    def get_coordinates(self):
        return {'x': self.x, 'y': self.y,
        'width': self.width, 'height': self.height}


class CircleButton(Button):
    def __init__(self, center_coordinates, radius):
        self.x, self.y = center_coordinates
        self.radius = radius

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
