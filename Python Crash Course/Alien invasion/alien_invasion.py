import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class for managing game resources and behavior"""

    def __init__(self):
        """Initialize the game resources and behavior"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the game"""
        while True:
            """Keyboard and mouse event tracking"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Each time the loop passes, the screen is redrawn"""
            self.screen.fill(self.settings.bg_color)
            """Display the last screen drawn"""
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
