class GameStats:
    """track statistics for alien Invasion."""


    def __init__(self, ai_game):
        """initalizing stats"""
        self.settings = ai_game. settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False

        # High Score should never reset.
        self.high_score = 0 


        


    def reset_stats(self):
        """Initializing stats that can change during the games."""
        self.ships_left = self.settings.ship_limit
        
        self.score = 0 
        self.level = 0 
            