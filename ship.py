import pygame 

class Ship:
    """ A class to mange the ship. """

    def __init__(self, ai_game):
        """ initialize the ship and set it starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_react = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_react.midbottom

        # Start a decimal valaue for the ships's horizontal position.
        self.x = float(self.rect.x)

        #movement flag 
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """updating the ships postion based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_react.right:
            self.x += self.settings.ship_speed    
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x     
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)    