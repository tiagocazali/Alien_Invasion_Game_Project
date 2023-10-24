class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's STATIC settings.
        Settings that DO NOT change"""
        
        #Screen Settings:
        self.isFullScreen = False
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship Settings:
        self.ship_lives = 3

        #Bullet Settingsg:
        self.bullet_width = 30 #3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        #Aliens Setting
        self.fleet_drop_speed = 10 #10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.3
        
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Initialize the dinamic settings
        self.initialize_dinamic_settings()
    

    def initialize_dinamic_settings(self):
        """Initialize settings that change throughout the game.
        Basically what changes is the Speed of the game!"""

        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 1 #1
        self.fleet_direction = 1  #1 represents right; -1 represents left.

        # Scoring settings - Value of each alien destroed 
        self.alien_points = 50


    def increase_speed(self):
        """Increase Speed Settings, make the Game Harder"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= self.score_scale
        #self.alien_points = int(self.alien_points * self.score_scale)