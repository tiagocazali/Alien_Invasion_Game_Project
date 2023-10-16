import sys
from turtle import right
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events() #Watch for keyboard and mouse events.
            self.ship.update() #Use the method update in Ship to move the Ship
            self._update_screen() #update de Screen
            self.clock.tick(60) #make the loop run exactly 60 times per second


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN: #Press the key
                if event.key == pygame.K_RIGHT: 
                    self.ship.moving_right = True #This variable are inside de Class Ship
                            
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP: #Release the right key
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False #This variable are inside de Class Ship
            
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        #Using the function in SHIP to criate the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()