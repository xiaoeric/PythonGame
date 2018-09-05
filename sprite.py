import pygame
import cv2
import numpy as np


class Sprite:
    def __init__(self, sprites=[]):
        self.sprites = sprites

    @classmethod
    def from_coord(cls, col, row, width, height, gap, filename):
        sprites = []
        ss = pygame.image.load(filename)
        for n in range(4):
            current_col = (col + n * (width + gap))
            rect = pygame.Rect(current_col, row, width, height)
            sprites.append(ss.subsurface(rect))
            # sprites.append(ss[row:row + height, current_col:current_col + width])
        for n in range(1, 3):
            sprites.insert(4, sprites[n])

        return cls(sprites)

    @classmethod
    def from_merge(cls, head_row, body_row):
        sprites = []
        for n in range(len(body_row.get_list())):
            head = head_row.get_list()[n]
            body = body_row.get_list()[n]
            body.blit(head, (6, 0))  # TODO: figure out where her head goes
            sprites.append(body)

        return cls(sprites)

    def get_list(self):
        return self.sprites

    def get_raw_list(self):
        return self.sprites

    @staticmethod
    def merge_alpha(image, alpha_mask):
        b_channel, g_channel, r_channel, _ = cv2.split(image)
        # TODO: resolve assertion error by alpha blending properly
        # https://www.learnopencv.com/alpha-blending-using-opencv-cpp-python/

        # Create alpha channel from the mask
        _, alpha_channel = cv2.threshold(alpha_mask, 0, 255, cv2.THRESH_BINARY)

        image_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
        cv2.imshow("img", image_BGRA)
        return image_BGRA

    @staticmethod
    def cvimage_to_pygame(image):
        # Convert cvimage into a pygame surface
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        image = cv2.transpose(image)
        surface = pygame.Surface(image.shape[:2], pygame.SRCALPHA)
        pygame.surfarray.blit_array(surface, image)
        surface = surface.convert_alpha()
        return surface
