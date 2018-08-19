import sys
import pygame
from dagger import Dagger
from faceless import Faceless


def check_events(ai_settings, screen, player, daggers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player, daggers)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event, ai_settings, screen, player, daggers):
    # Respond to key presses
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        player.moving_up = True
        # player.sprite_loop = player.moving_up_sprite
        # debug
        print('moving up')
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.moving_down = True
        # player.sprite_loop = player.moving_down_sprite
        # debug
        print('moving down')
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = True
        # player.sprite_loop = player.moving_left_sprite
        # debug
        print('moving left')
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.moving_right = True
        # player.sprite_loop = player.moving_right_sprite
        # debug
        print('moving right')
    if event.key == pygame.K_SPACE:
        # Create a new dagger and add it to the daggers group
        if len(daggers) < ai_settings.daggers_allowed:
            new_dagger = Dagger(ai_settings, screen, player)
            daggers.add(new_dagger)


def check_keyup_events(event, player):
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        player.moving_up = False
        # debug
        print('stop moving up')
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.moving_down = False
        # debug
        print('stop moving down')
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = False
        # debug
        print('stop moving left')
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.moving_right = False
        # debug
        print('stop moving right')
    if not player.is_moving:
        player.sprite_loop = player.stationary_sprite
        # debug
        print('stop moving')


def create_horde(ai_settings, screen, faceless_horde):
    """Create a full horde of Faceless"""
    # Create a Faceless and find the number of Faceless in a column
    # Spacing between each Faceless is equal to one Faceless height
    faceless = Faceless(ai_settings, screen)
    faceless_height = faceless.rect.height
    available_space_y = ai_settings.screen_width - 2 * faceless_height
    number_faceless_y = int(available_space_y / (2 * faceless_height))

    # Create the first row of Faceless
    for faceless_number in range(number_faceless_y):
        # Create a Faceless and place it in the row
        faceless = Faceless(ai_settings, screen)
        faceless.y = faceless_height + 2 * faceless_height * faceless_number
        faceless.rect.y = faceless.y
        faceless_horde.add(faceless)


def update_screen(ai_settings, screen, player, faceless_horde, daggers):
    screen.fill(ai_settings.bg_color)
    # Redraw all daggers behind player
    for dagger in daggers.sprites():
        dagger.draw_dagger()
    player.blitme()
    for faceless in faceless_horde:
        faceless.loop_sprite()
    faceless_horde.draw(screen)

    left = screen.get_rect().left

    # debug things
    # for n in range(4):
    #    sprite = player.stationary_sprite.get_list()[n]
    #    rect = sprite.get_rect()
    #    rect.left = left
    #    screen.blit(sprite, rect)
    #    left = rect.right

    pygame.display.flip()
