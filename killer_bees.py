import sys
import pygame as pg
import pygame.sprite

from settings import Settings
from ship import Ship


class KillerBees:
    """ Overall class to manage game assets and behaviour """
    def __init__(self):
        """ initialise the game and create game resources """
        pg.init()
        self.settings = Settings()
        # self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Killer Bees - v1")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ main loop for the game """
        while True:
            self._check_events()    # check for keyboard events
            self.ship.update()      # update the position of the ship
            self.bullets.update()
            # finally update the screen
            self._update_screen()   # update the screen


    def _check_events(self):
        """ Responds to key presses and mouse events """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to key presses """
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        self.ship.drawbee()
        pg.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    kb = KillerBees()
    kb.run_game()



