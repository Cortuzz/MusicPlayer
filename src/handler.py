import pygame


class Handler:
    def __init__(self, player, buttons):
        self.player = player
        self.buttons = buttons

    def mouse_events(self, event):
        if event.button == 1:
            for button in self.buttons:
                button.try_action(event.pos, self.player)

        if event.button == 4:
            self.player.change_volume(0.03)

        elif event.button == 5:
            self.player.change_volume(-0.03)

    def keyboard_events(self, event):
        if event.key == pygame.K_SPACE:
            self.player.change_pause()

        if event.key == pygame.K_m:
            self.player.change_mute()

        if event.key == pygame.K_UP:
            self.player.change_volume(0.05)
        elif event.key == pygame.K_DOWN:
            self.player.change_volume(-0.05)

        if event.key == pygame.K_RIGHT:
            self.player.change_position(5)
        elif event.key == pygame.K_LEFT:
            self.player.change_position(-5)
