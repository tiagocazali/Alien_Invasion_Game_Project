import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from buttom import Buttom
from game_stats import GameStats

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
        self.statistics = GameStats(self)    # Create an instance to store game statistics
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create the group that holds the bullets
        self.aliens = pygame.sprite.Group()  # Create the group that holds the Aliens
        self._create_fleet()
        self.game_active = False #This variable will control the loop for Game-Over

        self.play_buttom = Buttom(self, "Play") #Create the PLAY buttom
 

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()   #Watch for keyboard and mouse events.
            if self.game_active:    
                self.ship.update()     #Use the update method in Ship to move the Ship
                self._update_bullets() #call update() on a group, the group automatically calls update() for each sprite in the group. 
                self._update_aliens()  #Call update() on aliens Group, to make aliens move
            self._update_screen()  #update de Screen
            self.clock.tick(60)    #make the loop run exactly 60 times per second


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: #When the user click in the X to close windown. 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN: #Press any key
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP: #Release the key
                self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_click_in_play_buttom(mouse_position) #Check if the mouse click was in PLAY buttom


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


    def _check_click_in_play_buttom(self, mouse_position):
        """Start a new game when the player clicks Play."""

        #Check if the click was in PLAY button and if the game is INACTIVE:
        if self.play_buttom.rect.collidepoint(mouse_position) and not self.game_active:
            #reset the game statistics
            self.statistics.reset_stats()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

            self.game_active = True


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
        
        # After update bullets position, check if there is a Collision
        self._check_bullets_aliens_collision()
        

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions"""
        
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for alien hit the Bottom
        self._check_aliens_hit_bottom()


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

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_buttom.draw_buttum()

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
        
        #Fill the screen with aliens - Create a line, fill it and add another
        while current_y < (self.settings.screen_height - 4*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2*alien_height


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""

        for each_alien in self.aliens.sprites():
            if each_alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""

        for each_alien in self.aliens.sprites():
            each_alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_bullets_aliens_collision(self):
        """Respond to bullet-alien collisions."""
        
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #checking if after the collisions, all aliens were destroyed and create more
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        
        #check if the ship has more lives to play again
        if self.statistics.ship_lives > 0:
            # Decrement ships_lives
            self.statistics.ship_lives -= 1

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause the game for 5 seg.
            #So user can see that an Alien collided with the ship
            sleep(0.7)

        else:
            #There is no more lives, so stop the game
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_hit_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        
        for each_alien in self.aliens.sprites():
            if each_alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break 


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()