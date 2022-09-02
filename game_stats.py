class GameStats:
    """ Track statistics for Killer Bees """

    def __init__(self):
        """ Initialise statistics """
        self.settings = kb_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Initialise statistics that can change during game """
        self.ships_left = self.settings.ship_limit
