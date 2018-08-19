from abc import ABCMeta, abstractmethod
import pygame
import cv2


class Sprite(metaclass=ABCMeta):
    def __init__(self):
        self.sprites = []

    def get_list(self):
        pygame_imgs = []
        for image in self.sprites:
            pygame_imgs.append(self.cvimage_to_pygame(image))
        return pygame_imgs

    def get_raw_list(self):
        return self.sprites

    @staticmethod
    def cvimage_to_pygame(image):
        # Convert cvimage into a pygame surface
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.transpose(image)
        return pygame.surfarray.make_surface(image)
        # TODO: implement transparency using alpha channels
