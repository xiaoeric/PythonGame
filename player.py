from spriterow import SpriteRow
from spriteplayer import SpritePlayer

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
        self.stationary_body = SpriteRow(7, 1660, 22, 24, 10, ss_maid)
        self.moving_up_sprite = SpriteRow(7, 1792, 22, 24, 10, ss_maid)
        self.moving_down_sprite = SpriteRow(7, 1760, 22, 24, 10, ss_maid)
        self.moving_left_sprite = SpriteRow(7, 1698, 22, 24, 10, ss_maid)
        self.moving_right_sprite = SpriteRow(7, 1730, 22, 24, 10, ss_maid)

        # felicia head sprite rows
        self.stationary_head = SpriteRow(13, 8, 16, 15, 16, ss_felicia)

        # felicia maid sprite rows
        self.stationary_sprite = SpritePlayer(self.stationary_head, self.stationary_body)

        # stationary is default
        self.sprite_loop = self.stationary_sprite

        # start at the first frame
        self.sprite_index = float(0)

        # settings to change animation loop speed
        self.sprite_iter_speed = ai_settings.animation_speed

        # initialize image field
        self.image = self.get_image()

        # initialize rectangle of player
        self.rect = self.image.get_rect()

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
        if self.sprite_index >= 6:
            self.sprite_index = float(0)
        self.image = self.get_image()

    def get_image(self):
        # gets current image in sprite row
        return self.sprite_loop.get_list()[int(self.sprite_index)]

    def blitme(self):
        # load images and rectangles onto screen
        self.screen.blit(self.image, self.rect)
