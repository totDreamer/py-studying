import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Class to represent a one star"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Download star picture and set rect value
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Each new star appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


