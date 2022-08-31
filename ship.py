import pygame as pg


class Ship:
    """ A class to manage the spaceship! """

    def __init__(self, kb_game):
        """ Initialise the ship and set its starting position """
        self.screen = kb_game.screen
        self.settings = kb_game.settings
        self.screen_rect = kb_game.screen.get_rect()
        self.image = pg.image.load('/home/oem/Downloads/ship.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        # MOVEMENT FLAGS
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ships position based on MOVEMENT FLAGS """

        # Update the ship's x vale, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)


