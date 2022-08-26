import pygame as pg


class Ship:
    """ A class to manage the spaceship! """

    def __init__(self, kb_game):
        """ Initialise the ship and set its starting position """
        self.screen = kb_game.screen
        self.settings = kb_game.settings
        self.screen_rect = kb_game.screen.get_rect()
        self.image1 = pg.image.load('/home/oem/Downloads/ship.bmp')
        self.rect1 = self.image1.get_rect()
        self.image2 = pg.image.load('/home/oem/Downloads/bee-180.bmp')
        self.rect2 = self.image2.get_rect()

        # start each new ship at the bottom centre of the screen
        self.rect1.midbottom = self.screen_rect.midbottom
        self.rect2.midtop = self.screen_rect.midtop

        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect1.x)

        # MOVEMENT FLAGS
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ships position based on MOVEMENT FLAGS """

        # Update the ship's x vale, not the rect
        if self.moving_right and self.rect1.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect1.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x
        self.rect1.x = self.x

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image1, self.rect1)

    def drawbee(self):
        """ Draw the bee top centre screen  """
        self.screen.blit(self.image2, self.rect2)
