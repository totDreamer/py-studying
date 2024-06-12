class Settings:
    def __init__(self):
        """Initialize the static game settings"""
        # Display settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (25, 25, 112)
        # Ship settings
        self.ship_limit = 2
        # Bullet settings
        self.bullets_allowed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        # Aliens setting
        self.fleet_drop_speed = 20
        # Stars settings
        self.stars_speed = 0.1

        self.speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the dynamic game settings"""
        self.ship_speed_factor = 0.2
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed of the object"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.score_scale
