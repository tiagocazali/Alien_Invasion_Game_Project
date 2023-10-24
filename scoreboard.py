import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""

        self.screen = ai_game.screen
        self.screen_rec = self.screen.get_rect()
        self.settings = ai_game.settings
        self.statistics = ai_game.statistics

        #Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image:
        self.prep_score()


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


    def draw_score (self):
        """Draw score to the screen."""

        self.screen.blit(self.score_image, self.score_rect)

