import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load high score from a JSON file"""
        filename = 'D:\Python-Studying\json_files\high_score.json'
        try:
            with open(filename) as f:
                return json.load(f)
        except FileNotFoundError:
            return 0