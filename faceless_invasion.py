import pygame
from settings import Settings
from player import Player
import game_functions as gf
from pygame.sprite import Group
from pygame.time import Clock
from game_state import GameState as GS
from game_state import ScreenState as ScS


def run_game():
    clock = Clock()

    pygame.init()
    pygame.font.init()

    game_state = GS(GS.INVASION)
    screen_state = ScS(ScS.NONE)

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

    invasion_filename = 'images/Invasion Background.png'
    invasion_background = pygame.image.load(invasion_filename)
    invasion_background = pygame.transform.scale(invasion_background, (ai_settings.screen_width,
                                                                       ai_settings.screen_height))

    shop_filename = 'images/Awakening Support Background.jpg'
    shop_background = pygame.image.load(shop_filename)
    shop_background = pygame.transform.scale(shop_background, (ai_settings.screen_width, ai_settings.screen_height))

    while True:
        clock.tick(ai_settings.fps)
        # dt = clock.tick()
        # print(dt)

        gf.check_events(ai_settings, screen, player, daggers, game_state, screen_state)

        if game_state.get_state() == GS.INVASION or game_state.get_state() == GS.VICTORY:
            player.update(ai_settings)

        if game_state.get_state() == GS.INVASION:
            daggers.update()
            gf.update_daggers(ai_settings, screen, player, faceless_horde, daggers, game_state)
            gf.update_horde(ai_settings, faceless_horde)

        if screen_state.get_state() == ScS.FADE_OUT:
            if fade_alpha < 255:
                fade_alpha += ai_settings.fade_speed
                black_screen.set_alpha(fade_alpha)
            elif fade_alpha >= 255:
                if game_state.get_state() == GS.VICTORY:
                    game_state.set_state(GS.SHOP)
                elif game_state.get_state() == GS.SHOP:
                    game_state.set_state(GS.INVASION)
                screen_state.set_state(ScS.FADE_IN)

        if screen_state.get_state() == ScS.FADE_IN:
            if fade_alpha > 0:
                fade_alpha -= ai_settings.fade_speed
                black_screen.set_alpha(fade_alpha)
            elif fade_alpha <= 0:
                screen_state.set_state(ScS.NONE)

        gf.update_screen(ai_settings, screen, player, faceless_horde, daggers, black_screen, invasion_background, shop_background,
                         game_state, screen_state)

        pygame.display.set_caption("FPS: %i    Game State: %s    Screen State: %s" % (clock.get_fps(),
                                                                                      game_state.get_name(),
                                                                                      screen_state.get_name()))


run_game()
