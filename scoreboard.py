import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rec = self.screen.get_rect()
        self.settings = ai_game.settings
        self.statistics = ai_game.statistics

        #Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 38)

        #Prepare the initial score image:
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship_lives_image()
        

    def prep_score(self):
        """Turn the score into a rendered image."""

        # round the score value and format it as an String to show 1,000,000,000
        rounded_score = round(self.statistics.score)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rec.right -20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image."""

        high_score = round(self.statistics.high_score)
        high_score_str = f"High Score: {high_score:,}"
        self.higt_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.higt_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rec.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """Turn the level into a rendered image."""

        level_str = f"Level: {self.statistics.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 


    def prep_ship_lives_image(self):
        """Show how many ships are left in small figures on the Left top."""
        
        #This will create a line with 3 ships images - An Group
        self.ships = Group()
        for ship_number in range(self.statistics.ship_lives):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)


    def check_high_score(self):
        """Check to see if there's a new high score."""

        if self.statistics.score > self.statistics.high_score:
            self.statistics.high_score = self.statistics.score
            self.prep_high_score()


    def draw_score (self):
        """Draw scores, level, and ships to the screen."""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.higt_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen) #this is a Group, so the Method Draw is IN this group

