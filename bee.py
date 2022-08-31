import pygame as pg
from pygame.sprite import Sprite


class Bee(Sprite):
    """ A class to represent a single bee in the swarm """

    def __init__(self, kb_game):
        """ Initialize the bee and set its starting position """
        super().__init__()
        self.screen = kb_game.screen
        # Load the bee image and set its rect attribute
        self.image = pg.image.load('/home/oem/Downloads/bee-180.bmp')
        self.rect = self.image.get_rect()
        # Start each new bee near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)