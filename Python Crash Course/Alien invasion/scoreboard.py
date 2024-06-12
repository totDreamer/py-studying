import pygame.font

class Scoreboard():
    """Scoreboard class"""

    def __init__(self, ai_game):
        """Initialize atribute for scoring"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 24)
        self.prep_score()

    def prep_score(self):
        """Convert score to image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -10
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)