import pygame as pg


class Settings:
    """ A Class to store all settings for the Alien Invasion game """

    def __init__(self):
        """ Intitialise game settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (253, 254, 254)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)


