import pygame
import cv2


class Sprite:
    def __init__(self, sprites=[]):
        self.sprites = sprites

    @classmethod
    def from_coord(cls, col, row, width, height, gap, filename):
        sprites = []
        ss = cv2.imread(filename, cv2.IMREAD_UNCHANGED)  # spritesheet.spritesheet(filename)
        for n in range(4):
            current_col = (col + n * (width + gap))
            sprites.append(ss[row:row + height, current_col:current_col + width])
        for n in range(1, 3):
            sprites.insert(4, sprites[n])

        return cls(sprites)

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
