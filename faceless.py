import pygame
from pygame.sprite import Sprite as PySprite
from sprite import Sprite


class Faceless(PySprite):
    """A class to represent a single Faceless in the horde"""

    def __init__(self, ai_settings, screen):
        """Initialize the Faceless and set its starting position"""
        super(Faceless, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # filename for spritesheet
        ss_faceless = 'images/3DS - Fire Emblem Fates - Faceless.png'

        # faceless sprite row
        self.moving_left = Sprite.from_coord(6, 39, 23, 27, 10, ss_faceless)
        self.moving_right = Sprite.from_coord(4, 71, 23, 27, 9, ss_faceless)

        self.sprite_loop = self.moving_right

        self.sprite_index = float(0)

        # settings to change animation loop speed
        self.sprite_iter_speed = ai_settings.animation_speed

        # Load the Faceless image and set its rect attribute
        self.image = self.get_image()
        self.rect = self.image.get_rect()

        # Start each new Faceless near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Faceless' exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if Faceless is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        """Move the Faceless down or up"""
        self.y += (self.ai_settings.faceless_speed_factor * self.ai_settings.horde_direction)
        self.rect.y = self.y
        self.loop_sprite()

    def loop_sprite(self):
        self.sprite_index += self.sprite_iter_speed
        if self.sprite_index >= 6:
            self.sprite_index = float(0)
        self.image = self.get_image()

    def get_image(self):
        # gets current image in sprite row
        return self.sprite_loop.get_list()[int(self.sprite_index)]

    def blitme(self):
        # load images and rectangles onto screen
        self.loop_sprite()
        self.screen.blit(self.image, self.rect)
