import pygame as pg
from pygame.sprite import Sprite


class Bee(Sprite):
    """ A class to represent a single bee in the swarm """

    def __init__(self, kb_game):
        """ Initialize the bee and set its starting position """
        super().__init__()
        self.screen = kb_game_screen
