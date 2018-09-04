import pygame
import cv2
import numpy as np


class Sprite:
    def __init__(self, sprites=[]):
        self.sprites = sprites

    @classmethod
    def from_coord(cls, col, row, width, height, gap, filename):
        sprites = []
        alpha_channels = []
        ss = cv2.imread(filename, cv2.IMREAD_UNCHANGED)  # spritesheet.spritesheet(filename)
        for n in range(4):
            current_col = (col + n * (width + gap))
            sprites.append(ss[row:row + height, current_col:current_col + width])

            alpha_channels.append(ss[row:row + height, current_col + 128:current_col + 128 + width])

            sprites[n] = cls.merge_alpha(sprites[n], alpha_channels[n])
        for n in range(1, 3):
            sprites.insert(4, sprites[n])

        return cls(sprites)

    @classmethod
    def from_merge(cls, head, body):
        sprites = []

    def get_list(self):
        pygame_imgs = []
        for image in self.sprites:
            pygame_imgs.append(self.cvimage_to_pygame(image))
        return pygame_imgs

    def get_raw_list(self):
        return self.sprites

    @staticmethod
    def merge_alpha(image, alpha_channel):
        b_channel, g_channel, r_channel, _ = cv2.split(image)
        # TODO: resolve assertion error by alpha blending properly
        # https://www.learnopencv.com/alpha-blending-using-opencv-cpp-python/
        alpha_channel = alpha_channel.astype(float)/255
        image_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
        return image_BGRA

    @staticmethod
    def cvimage_to_pygame(image):
        # Convert cvimage into a pygame surface
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        image = cv2.transpose(image)
        return pygame.surfarray.make_surface(image)
