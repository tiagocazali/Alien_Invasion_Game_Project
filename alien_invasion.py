import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        #Check if Full Screen is set to True in Settings
        if self.settings.isFullScreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_height = self.screen.get_rect().height
            self.settings.screen_width = self.screen.get_rect().width
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create the group that holds the bullets
        self.aliens = pygame.sprite.Group()  # Create the group that holds the Aliens
        self._create_fleet()


    
    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()  #Watch for keyboard and mouse events.
            self.ship.update()    #Use the update method in Ship to move the Ship
            self._update_bullets() #call update() on a group, the group automatically calls update() for each sprite in the group. 
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
        
        #check if the user have avalible bullets to use
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        
        #update bullets positions
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        #go to all bullets in the screen and re-draw it in the correct position
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Using the function in SHIP to criate the ship
        self.ship.draw_ship()

        #To make the alien appear, we need to call the group’s draw() method
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        # Make an single alien just to take his hidth and height
        temp = Alien(self)
        alien_width = temp.rect.width
        alien_height = temp.rect.height
        
        current_x, current_y = alien_width, alien_height
        
        #Creating a line of alines
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._creat_alien(current_x, current_y)
                current_x += 2*alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2*alien_height

    def _creat_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()