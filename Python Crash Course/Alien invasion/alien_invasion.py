import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:
    """Class for managing game resources and behavior"""

    def __init__(self):
        """Initialize the game resources and behavior"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._create_stars()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_stars()
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

    def _update_bullets(self):
        self.bullets.update()
        # Removing bullets that went off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Checking Alien Hit
        # If a hit is detected, remove the projectile and the alien
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Checking Alien Hit, remove it and build new fleet"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy bullets and make new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Updates alien on fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Detects if aliens have reached the screen border"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                self._update_stars()
                break

    def _change_fleet_direction(self):
        """Lowers the entire fleet and changes direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_stars(self):
        """Creates a stars"""
        # Create and calculate the number of stars
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width
        available_space_y = self.settings.screen_height
        max_stars = available_space_x // (star_width * 2)
        stars_count = randint(13, max_stars)
        for _ in range(stars_count):
            self._create_one_star()

    def _create_one_star(self):
        """Creates one star"""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width
        available_space_y = self.settings.screen_height
        star.rect.x = randint(0, available_space_x - star_width)
        star.rect.y = randint(0, available_space_y - star_height)
        star.y = float(star.rect.y)  # Use a float for precise vertical position
        self.stars.add(star)

    def _update_stars(self):
        for star in self.stars.sprites():
            star.y += self.settings.stars_speed
            star.rect.y = int(star.y)  # Update rect.y to the nearest integer
            # If the star goes below the screen, reset its position to the top
            if star.rect.top >= self.settings.screen_height:
                star.y = 0 - star.rect.height
                star.rect.x = randint(0, self.settings.screen_width - star.rect.width)
        self.stars.update()

    def _create_fleet(self):
        """Creates a fleet"""
        # Create and calculating the number of aliens in a row
        #  The interval between the two is equal to the width of the alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determines the number of rows that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (5 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create a fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Creates an alien and adds it to the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Each time the loop passes, the screen is redrawn"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Creating a new projectile and adding it to the group 'bullet'"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
