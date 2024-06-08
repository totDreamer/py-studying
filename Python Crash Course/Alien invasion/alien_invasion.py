import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for managing game resources and behavior"""

    def __init__(self):
        """Initialize the game resources and behavior"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Handles keystrokes and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Each time the loop passes, the screen is redrawn"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Display the last screen drawn
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
