class GameStats:
    """Track statistics for Killer Bees"""
    def __init__(self, kb_game):
        """Initialize statistics."""
        self.settings = kb_game.settings
        self.reset_stats()

        # Start Killer Bees in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
