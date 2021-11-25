import gui

class Button:
    def __init__(self, left_top, right_bottom, action):
        '''
        Input two tuples of pairs of coordinates
        '''

        self.left_top = left_top
        self.right_bot = right_bottom
        self.action = action
        self.is_pressed = False

        self.exception_handler()

    def exception_handler():
        if not(isinstance(self.left_top, tuple) and isinstance(self.right_bottom, tuple)):
            raise TypeError(
            "Object Button takes 2 tuples but {} and {} were given".format(
            type(self.left_top), type(self.right_bottom)))

        if not (len(self.left_top) == 2 and len(self.right_bottom) == 2):
            raise ValueError(
            "Tuples left_top and right_bottom contains 2 coordinates \
            but {} and {} were given".format(
            len(self.left_top), len(self.right_bottom)))

        # TODO : check for float value

    def if_pressed(self):
        if(True):  #TODO: from gui check if mouse is on button and clicked
            self.Press()

class Pause(Button):
    def press(self):
        pass

a = Button(4, (56, 2))
