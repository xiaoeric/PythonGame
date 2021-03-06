import pygame
from pygame.font import Font


class Settings:

    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        self.fps = 60
        self.fade_speed = 5

        self.player_speed_factor = 2.5 * 60.0 / self.fps

        self.animation_speed = 6.0 / self.fps

        # Dagger settings
        self.dagger_speed_factor = 9 * 60.0 / self.fps
        self.dagger_width = 15
        self.dagger_height = 3
        self.dagger_color = 60, 60, 60
        self.daggers_allowed = 3

        # Faceless settings
        self.faceless_speed_factor = 1 * 60.0 / self.fps
        self.horde_crawl_speed = 10 * 60.0 / self.fps
        # horde direction of 1 represents down; -1 represents up
        self.horde_direction = 1

        self.font_name = pygame.font.get_default_font()
        self.font_size = 18
        self.font = Font(self.font_name, self.font_size)
