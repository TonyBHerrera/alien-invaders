class Settings:
    """ A Class to store and the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games's static settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        
        
        # Ship Speed
        self.ship_limit = 3  
        
        
        # bullet settings
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 100
        
        #alien settings
        self.fleet_drop_speed = 10 

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
        
        
    def initialize_dynamic_settings(self):
        """ INitialize settings that change throughout the game. """
        self.ship_speed = 3
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left. 
        self.fleet_direction = 1 


        #  Scoring 
        self.alien_points = 50 

    def increase_speed(self):
        """ Increse speed settings and alien point values. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien_points