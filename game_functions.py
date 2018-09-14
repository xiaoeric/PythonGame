import sys
import pygame
from dagger import Dagger
from faceless import Faceless
import game_state as gs


def check_events(ai_settings, screen, player, daggers, game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player, daggers, game_state)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event, ai_settings, screen, player, daggers, game_state):
    # Respond to key presses
    if game_state.get_state() == gs.VICTORY:
        # TODO: add victory closing animation here
        game_state.set_state(gs.FADE_OUT)
    elif game_state.get_state() == gs.INVASION:
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


def check_horde_edges(ai_settings, faceless_horde):
    """Respond appropriately if any Faceless have reached an edge"""
    for faceless in faceless_horde.sprites():
        if faceless.check_edges():
            change_horde_direction(ai_settings, faceless_horde)
            break


def change_horde_direction(ai_settings, faceless_horde):
    """Crawl the entire horde and change the horde's direction"""
    ai_settings.horde_direction *= -1
    for faceless in faceless_horde.sprites():
        # For some reason incrementing faceless.x by crawl_speed
        # and then assigning faceless.x to faceless.rect.x will cause
        # the entire horde to disappear except for one column
        faceless.rect.x += ai_settings.horde_crawl_speed


def get_number_faceless_y(ai_settings, faceless_height):
    """Determine the number of Faceless that fit in a column"""
    available_space_y = ai_settings.screen_height - 2 * faceless_height
    number_faceless_y = int(available_space_y / (2 * faceless_height))
    return number_faceless_y


def get_number_cols(ai_settings, player_width, faceless_width):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_x = (ai_settings.screen_width - (3 * faceless_width) - player_width)
    number_cols = int(available_space_x / (2 * faceless_width))
    return number_cols


def create_faceless(ai_settings, screen, faceless_horde, faceless_number, col_number):
    """Create a Faceless and place it in the row"""
    faceless = Faceless(ai_settings, screen)
    faceless_height = faceless.rect.height
    faceless.y = faceless_height + 2 * faceless_height * faceless_number
    faceless.rect.y = faceless.y
    faceless.rect.x = faceless.rect.width + 2 * faceless.rect.width * col_number
    faceless_horde.add(faceless)


def create_horde(ai_settings, screen, player, faceless_horde):
    """Create a full horde of Faceless"""
    # Create a Faceless and find the number of Faceless in a column
    # Spacing between each Faceless is equal to one Faceless height
    faceless = Faceless(ai_settings, screen)
    number_faceless_y = get_number_faceless_y(ai_settings, faceless.rect.height)
    number_cols = get_number_cols(ai_settings, player.rect.width, faceless.rect.width)

    # Create the horde of Faceless
    for col_number in range(number_cols):
        for faceless_number in range(number_faceless_y):
            create_faceless(ai_settings, screen, faceless_horde, faceless_number, col_number)


def update_horde(ai_settings, faceless_horde):
    """
    Check if the horde is at an edge
    and then update the positions of all Faceless in the horde
    """
    check_horde_edges(ai_settings, faceless_horde)
    faceless_horde.update()


def update_daggers(ai_settings, screen, player, faceless_horde, daggers, game_state):
    """Update position of daggers and get rid of old daggers"""
    # Get rid of daggers that have disappeared
    for dagger in daggers.copy():
        if dagger.rect.right <= 0:
            daggers.remove(dagger)

    check_dagger_faceless_collisions(ai_settings, screen, player, faceless_horde, daggers, game_state)


def check_dagger_faceless_collisions(ai_settings, screen, player, faceless_horde, daggers, game_state):
    """Respond to dagger-Faceless collisions"""
    if len(faceless_horde) == 0:
        #  Destroy existing daggers and create new horde
        daggers.empty()
        game_state.set_state(gs.VICTORY)
        # TODO: play victory opening animation
        # create_horde(ai_settings, screen, player, faceless_horde)

    # Checking for collisions after checking for horde generation will delay respawning
    # to the next loop, allowing the last Faceless sprite to disappear.
    collisions = pygame.sprite.groupcollide(daggers, faceless_horde, True, True)


def update_screen(ai_settings, screen, player, faceless_horde, daggers, fade_layer):
    screen.fill(ai_settings.bg_color)
    # Redraw all daggers behind player
    for dagger in daggers.sprites():
        dagger.draw_dagger()
    player.blitme()
    # for faceless in faceless_horde:
    #    faceless.loop_sprite()
    faceless_horde.draw(screen)

    screen.blit(fade_layer, (0, 0))

    left = screen.get_rect().left

    # debug things
    # for n in range(4):
    #    sprite = player.stationary_sprite.get_list()[n]
    #    rect = sprite.get_rect()
    #    rect.left = left
    #    screen.blit(sprite, rect)
    #    left = rect.right

    pygame.display.flip()
