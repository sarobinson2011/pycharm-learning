class GameStats:
    """Track statistics for Killer Bees"""
    def __init__(self, kb_game):
        """Initialize statistics."""
        self.settings = kb_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
