from sprite import Sprite
import pygame

# debug
# import time


class Player:
    def __init__(self, ai_settings, screen):
        # initialize screen and ai_settings as fields
        self.screen = screen
        self.ai_settings = ai_settings

        # filename for maid sprite sheet
        ss_maid = 'images/3DS - Fire Emblem Fates - Maid.png'
        ss_felicia = 'images/3DS - Fire Emblem Fates - Felicia.png'

        # TODO: refactor for better organization
        # maid body sprite rows
        self.stationary_body = Sprite.from_coord(7, 1660, 22, 24, 10, ss_maid, 6)
        self.moving_up_body = Sprite.from_coord(7, 1792, 22, 24, 10, ss_maid, 4)
        self.moving_down_body = Sprite.from_coord(7, 1760, 22, 24, 10, ss_maid, 4)
        self.moving_left_body = Sprite.from_coord(7, 1698, 22, 24, 10, ss_maid, 4)
        # 7, 1730, 22, 24, 10, ss_maid, 4
        # 1726, ss_maid, 4
        self.moving_right_body = Sprite.from_coord(7, 1730, 22, 24, 10, ss_maid, 4)

        # felicia head sprite rows
        self.stationary_head = Sprite.from_coord(7, 8, 22, 15, 10, ss_felicia, 6)  # 13, 8, 16, 15, 16
        self.moving_up_head = Sprite.from_coord(7, 172, 22, 15, 10, ss_felicia, 4)
        self.moving_down_head = Sprite.from_coord(7, 140, 22, 15, 10, ss_felicia, 4)
        # TODO: redo coordinates for left head; third frame cuts some hair
        self.moving_left_head = Sprite.from_coord(7, 76, 22, 15, 10, ss_felicia, 4)
        # 7, 108, 22, 15, 10, ss_felicia, 4
        # 102, ss_felicia, 4
        self.moving_right_head = Sprite.from_coord(7, 108, 22, 15, 10, ss_felicia, 4)

        # felicia maid sprite rows
        self.stationary_sprite = Sprite.from_merge(self.stationary_head, self.stationary_body, (0, 1))
        self.moving_up_sprite = Sprite.from_merge(self.moving_up_head, self.moving_up_body, (0, 1))
        self.moving_down_sprite = Sprite.from_merge(self.moving_down_head, self.moving_down_body, (0, 1))
        self.moving_left_sprite = Sprite.from_merge(self.moving_left_head, self.moving_left_body, (0, 1))
        self.moving_right_sprite = Sprite.from_merge(self.moving_right_head, self.moving_right_body, (0, 1))

        # stationary is default
        self.sprite_loop = self.stationary_sprite

        # start at the first frame
        self.sprite_index = float(0)

        # settings to change animation loop speed
        self.sprite_iter_speed = ai_settings.animation_speed

        # initialize image field
        self.image = self.get_image()

        # initialize rectangle of player
        self.rect = self.get_rect()

        # get screen rectangle for reference
        self.screen_rect = screen.get_rect()

        # player is positioned in the center horizontally on the right of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # float conversion necessary for slower movement below 1 px per loop
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # initialize booleans to record moving status
        self.moving_up, self.moving_down, self.moving_left, self.moving_right, self.is_moving = (False,) * 5

    def update(self, ai_settings):
        # update player position based on moving status and position on screen
        if self.moving_up:
            self.sprite_loop = self.moving_up_sprite
            if self.rect.top > 0:
                self.centery -= ai_settings.player_speed_factor
        if self.moving_down:
            self.sprite_loop = self.moving_down_sprite
            if self.rect.bottom < self.screen_rect.bottom:
                self.centery += ai_settings.player_speed_factor
        if self.moving_left:
            self.sprite_loop = self.moving_left_sprite
            if self.rect.left > 0:
                self.centerx -= ai_settings.player_speed_factor
        if self.moving_right:
            self.sprite_loop = self.moving_right_sprite
            if self.rect.right < self.screen_rect.right:
                self.centerx += ai_settings.player_speed_factor

        # updates position of player rectangle; casts to int
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        # defines is_moving
        prev_move_status = self.is_moving
        self.is_moving = not (self.moving_up == self.moving_down) or not (self.moving_left == self.moving_right)
        if prev_move_status is not self.is_moving:
            print('Is moving: %s' % self.is_moving)

        # debug
        # if self.sprite_index == 0:
        # 	self.start_time = time.time()
        # if self.sprite_index == 5:
        # 	self.end_time = time.time()
        # 	self.fps = 6.0 / (self.end_time - self.start_time)
        # 	print(self.fps)

        # iterating sprite animation
        self.sprite_index += self.sprite_iter_speed
        if self.sprite_index >= 12:
            self.sprite_index = float(0)
        self.image = self.get_image()

    def get_image(self):
        # gets current image in sprite row
        return self.sprite_loop.get_list()[int(self.sprite_index) % self.sprite_loop.get_frames()]

    def get_rect(self):
        return self.get_image().get_bounding_rect()

    def blitme(self):
        # load images and rectangles onto screen
        self.screen.blit(self.image, self.rect)

        # debugging player sprite loop
        multiplier = 4

        # height = None
        # for n in range(self.sprite_loop.get_frames()):
        #     sprite = pygame.transform.scale2x(pygame.transform.scale2x(self.sprite_loop.get_list()[n]))
        #     if n == 0:
        #         height = sprite.get_size()[1]
        #     self.screen.blit(sprite, (n * sprite.get_size()[0], 0))
        #
        # self.screen.blit(pygame.transform.scale(self.image, (self.image.get_size()[0] * 4, height)), (0, height))
