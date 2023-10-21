class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        
        #Screen Settings:
        self.isFullScreen = False
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship Settings:
        self.ship_speed = 1.5
        self.ship_lives = 3

        #Bullet Settingsg:
        self.bullet_speed = 2.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        #Aliens Setting
        self.alien_speed = 10 #1
        self.fleet_drop_speed = 30 #10
        self.fleet_direction = 1 # 1 represents right; -1 represents left.