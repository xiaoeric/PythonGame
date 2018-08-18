import pygame
from pygame.sprite import Sprite


class Dagger(Sprite):
    # A class to manage daggers fired from the ship

    def __init__(self, ai_settings, screen, player):
        """Create a dagger object at the player's current position"""
        super(Dagger, self).__init__()
        self.screen = screen

        # Create a dagger rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.dagger_width,
                                ai_settings.dagger_height)
        self.rect.centery = player.rect.centery
        self.rect.left = player.rect.left

        # Store the dagger's position as a decimal value
        self.x = float(self.rect.x)

        self.color = ai_settings.dagger_color
        self.speed_factor = ai_settings.dagger_speed_factor

    def update(self):
        """Move the dagger left across the screen"""
        # Update the decimal position of the dagger
        self.x -= self.speed_factor
        # Update the rect position
        self.rect.x = self.x

    def draw_dagger(self):
        """Draw the dagger to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)