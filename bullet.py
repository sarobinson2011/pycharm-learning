import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullet firing """

    def __init__(self, kb_game):
        """ Create a bullet object at the ship's current position """
        super().__init__()
        self.screen = kb_game.screen
        self.settings = kb_game.settings
        self.colour = self.settings.bullet_colour

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = kb_game.ship.rect1.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen """
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen """
        pg.draw.rect(self.screen, self.colour, self.rect)
