class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize static statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize moved statistics"""
        self.ships_left = self.settings.ship_limit
        self.score = 0