import pygame
from settings import Settings
from player import Player
import game_functions as gf
from pygame.sprite import Group
from pygame.time import Clock
from faceless import Faceless


def run_game():
    clock = Clock()

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Faceless Invasion")

    # Make a player
    player = Player(ai_settings, screen)
    # Make a group to store daggers in
    daggers = Group()
    # Make a Faceless group
    faceless_horde = Group()

    # Create the horde of faceless
    gf.create_horde(ai_settings, screen, player, faceless_horde)

    while True:
        clock.tick(ai_settings.fps)
        # dt = clock.tick()
        # print(dt)

        gf.check_events(ai_settings, screen, player, daggers)
        player.update(ai_settings)
        daggers.update()

        # Get rid of daggers that have disappeared
        for dagger in daggers.copy():
            if dagger.rect.right <= 0:
                daggers.remove(dagger)
        # debug
        # print(len(daggers))
        gf.update_horde(ai_settings, faceless_horde)

        gf.update_screen(ai_settings, screen, player, faceless_horde, daggers)

        pygame.display.set_caption("FPS: %i" % clock.get_fps())


run_game()
