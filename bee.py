import pygame as pg
from pygame.sprite import Sprite


class Bee(Sprite):
    """ A class to represent a single bee in the swarm """

    def __init__(self, kb_game):
        """ Initialize the bee and set its starting position """
        super().__init__()
        self.screen = kb_game.screen
        self.settings = kb_game.settings

        # Load the bee image and set its rect attribute
        self.image = pg.image.load('/home/oem/Downloads/bee-180.bmp')
        self.rect = self.image.get_rect()

        # Start each new bee near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the bee's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return true if a bee is at the edge of the screen """
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right
                or self.rect.left <= 0):
            return True

    def update(self):
        """ Move the bee left or right """
        self.x += (self.settings.bee_speed *
                   self.settings.swarm_direction)
        self.rect.x = self.x

