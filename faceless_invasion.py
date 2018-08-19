import pygame
from settings import Settings
from player import Player
import game_functions as gf
from pygame.sprite import Group
from faceless import Faceless


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Faceless Invasion")

    # Make a player
    player = Player(ai_settings, screen)
    # Make a group to store daggers in
    daggers = Group()
    # Make a Faceless
    faceless = Faceless(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, player, daggers)
        player.update(ai_settings)
        daggers.update()

        # Get rid of daggers that have disappeared
        for dagger in daggers.copy():
            if dagger.rect.right <= 0:
                daggers.remove(dagger)
        # debug
        # print(len(daggers))

        gf.update_screen(ai_settings, screen, player, faceless, daggers)


run_game()
