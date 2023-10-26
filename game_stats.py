class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""

        self.settings = ai_game.settings
        self.high_score = 0 # High score should never be reset.
        self.reset_stats() # Call the method to create the First Statistic
    

    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        #change the atual ship lives for the standard in Settings
        self.ship_lives = self.settings.ship_lives
        self.score = 0
        self.level = 1