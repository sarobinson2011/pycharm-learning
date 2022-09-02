class Settings:
    """ A Class to store all settings for the Killer Bees game """

    def __init__(self):
        """ Initialize game settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (255, 255, 240)

        # Ship settings
        self.ship_speed = 1.5

        # Bee settings
        self.bee_speed = 3
        self.swarm_drop_speed = 10
        # Swarm direction: 1 = right, -1 = left
        self.swarm_direction = 1

        # Bullet settings
        self.bullet_speed = 1.8
        self.bullet_colour = (192, 192, 192)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3


