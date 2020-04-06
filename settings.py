class Settings:
    """ A Class to store and the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        # Ship Speed
        self.ship_speed = 1.5
        # bullet settings
        self.bullet_speed = 1.75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10
        #alien settings
        self.alien_speed = 1.0
        self.ship_limit = 3  
        self.fleet_drop_speed = 10 
        # fleet_direction of 1 represents right; -1 represents left. 
        self.fleet_direction = 1 
        
