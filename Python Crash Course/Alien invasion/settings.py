class Settings:
    def __init__(self):
        # Display size
        self.screen_width = 800
        self.screen_height = 600
        # Ship speed
        self.ship_speed = 0.2
        # Background color
        self.bg_color = (25, 25, 112)
        # Settings for bullet
        self.bullet_speed = 0.5
        self.bullets_allowed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        # Settings for aliens
        self.alien_speed = 0.05
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # Settings for stars
        self.stars_speed = 0.1