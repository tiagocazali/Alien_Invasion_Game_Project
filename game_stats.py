class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""

        self.settings = ai_game.settings
        self.reset_stats() #Call the method to create the First Statistic
    

    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ship_lives = self.settings.ship_lives