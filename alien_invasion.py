import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group() # create the group that holds the bullets
        
        #Check if Full Screen is set to True in Settings
        if self.settings.isFullScreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_height = self.screen.get_rect().height
            self.settings.screen_width = self.screen.get_rect().width
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()  #Watch for keyboard and mouse events.
            self.ship.update()    #Use the update method in Ship to move the Ship
            self.bullets.update() #call update() on a group, the group automatically calls update() for each sprite in the group. 
            self._update_screen() #update de Screen
            self.clock.tick(60)   #make the loop run exactly 60 times per second


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: #When the user click in the X to close windown. 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN: #Press any key
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP: #Release the key
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Responding to Keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
        
        elif event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True
                            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

        
    def _check_keyup_events(self, event):    
        """Responding to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False #This variable are inside de Class Ship
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 


    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Using the function in SHIP to criate the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()