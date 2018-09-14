import pygame
from settings import Settings
from player import Player
import game_functions as gf
from pygame.sprite import Group
from pygame.time import Clock
import game_state as gs


def run_game():
    clock = Clock()

    pygame.init()
    pygame.font.init()

    game_state = gs.GameState(gs.INVASION)

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

    black_screen = pygame.Surface((ai_settings.screen_width, ai_settings.screen_height))
    black_screen.fill((0, 0, 0))
    black_screen.set_alpha(0)
    fade_alpha = 0

    while True:
        clock.tick(ai_settings.fps)
        # dt = clock.tick()
        # print(dt)

        gf.check_events(ai_settings, screen, player, daggers, game_state)

        if game_state.get_state() == gs.INVASION or game_state.get_state() == gs.VICTORY \
                or game_state.get_state() == gs.FADE_OUT:
            player.update(ai_settings)

        if game_state.get_state() == gs.INVASION:
            daggers.update()
            gf.update_daggers(ai_settings, screen, player, faceless_horde, daggers, game_state)
            gf.update_horde(ai_settings, faceless_horde)

        if game_state.get_state() == gs.FADE_OUT:
            if fade_alpha < 255:
                fade_alpha += ai_settings.fade_speed
                black_screen.set_alpha(fade_alpha)

        gf.update_screen(ai_settings, screen, player, faceless_horde, daggers, black_screen)

        pygame.display.set_caption("FPS: %i    Game State: %s" % (clock.get_fps(), game_state.get_name()))


run_game()
