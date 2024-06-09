import pygame
from pygame.sprite import Sprite

class BulletRight(Sprite):
    """Class for controlling projectiles fired by a ship"""
    def __init__(self, ai_game):
        """Creates a projectile object at the current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

    # Creating a projectile at the zero position and assigning the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        # The projectile position is stored in float format
        self.x = float(self.rect.x)

    def update(self):
        """Updates the bullet position"""
        # Update in float format
        self.x += self.settings.bullet_speed
        # Update rectangle position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draws the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)