class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        
        #Screen Settings:
        self.isFullScreen = True
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship Settings:
        self.ship_speed = 1.5

        #Bullet Settingsg:
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 300