class GameStats:
    """track statistics for alien Invasion."""


    def __init__(self, ai_game):
        """initalizing stats"""
        self.settings = ai_game. settings
        self.reset_stats()


    def reset_stats(self):
        """Initializing stats that can change during the games."""
        self.ships_left = self.settings.ship_limit
            