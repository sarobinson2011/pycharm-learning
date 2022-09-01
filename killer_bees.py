import sys
import pygame as pg
import pygame.sprite
import random as rd

from settings import Settings
from ship import Ship
from bullet import Bullet
from bee import Bee


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
        self.bullets = pygame.sprite.Group()        # bullets group
        self.bees = pygame.sprite.Group()           # bees group - "the swarm"
        self._create_swarm()

    def run_game(self):
        """ main loop for the game """
        while True:
            # self._load_background()
            self._check_events()    # check for keyboard events
            self.ship.update()      # update the position of the ship
            self._update_bullets()  #
            self._update_bees()     #
            self._update_screen()   #

    # def _load_background(self):     # todo
    #     """ Loads the game background image """
    #     self.background = pg.image.load('/home/oem/Downloads/honeycomb.bmp')
    #     pg.transform.scale(self.background, (self.settings.screen_width, self.settings.screen_height))

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
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets """
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bees.draw(self.screen)

        pg.display.flip()

    def _create_bee(self, bee_number, row_number):
        # Create a bee and place it in the row
        bee = Bee(self)
        bee_width, bee_height = bee.rect.size
        bee.x = bee_width + 2 * bee_width * bee_number
        bee.rect.x = bee.x
        bee.rect.y = bee_height + 1.7 * bee.rect.height * row_number
        self.bees.add(bee)

    def _create_swarm(self):
        """ Create the swarm of bees """
        # Create a bee & find how many bees fit on a row (spacing = 1 bee width)
        bee = Bee(self)
        bee_width, bee_height = bee.rect.size
        available_space_x = self.settings.screen_width - (6 * bee_width)
        number_bees_x = available_space_x // (2 * bee_width)

        # Determine the number of rows of bees that fit on the screen
        ship_height = self.ship.rect.height
        # rand_int = rd.randint(6, 14)
        rand_int = 6
        available_space_y = (self.settings.screen_height - (rand_int * bee_height) - ship_height)
        number_rows = available_space_y // (2 * bee_height)

        # Create the full swarm of bees
        for row_number in range(number_rows):
            for bee in range(number_bees_x):
                self._create_bee(bee, row_number)

    def _update_bees(self):
        """
        Check if the swarm is at an edge, then
        update the positions of all bees in the swarm
        """
        self._check_swarm_edges()
        self.bees.update()

    def _check_swarm_edges(self):
        """ Respond appropriately if a bee has reached the screen edge """
        for bee in self.bees.sprites():
            if bee.check_edges():
                self._change_swarm_direction()
                break

    def _change_swarm_direction(self):
        """ Drop the entire swarm and change the swarm direction"""
        for bee in self.bees.sprites():
            bee.rect.y += self.settings.swarm_drop_speed
        self.settings.swarm_direction *= -1


if __name__ == '__main__':
    # make a game instance and run the game
    kb = KillerBees()
    kb.run_game()



