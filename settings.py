class Settings:
    """ A Class to store all settings for the Killer Bees game """

    def __init__(self):
        """ Initialize the game's statis settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (255, 255, 240)

        # Ship settings
        self.ship_speed = 1.5
        # Number of lives
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 1.8
        self.bullet_colour = (81, 90, 90)
        self.bullet_width = 4
        self.bullet_height = 14
        self.bullets_allowed = 3

        # Bee settings
        self.bee_speed = 1
        self.swarm_drop_speed = 8
        # Swarm direction: 1 = right, -1 = left
        self.swarm_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """ Initialise settings that change throughout the game """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.bee_speed = 1.0
        # Swarm direction: 1 = right, -1 = left
        self.swarm_direction = 1

    def increase_speed(self):
        """ Increase speeed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bee_speed *= self.speedup_scale










