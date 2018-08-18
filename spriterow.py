import cv2
from sprite import Sprite


class SpriteRow(Sprite):
    sprites = []

    def __init__(self, col, row, width, height, gap, filename):
        super().__init__()

        ss = cv2.imread(filename, cv2.IMREAD_UNCHANGED)  # spritesheet.spritesheet(filename)
        for n in range(4):
            current_col = (col + n * (width + gap))
            self.sprites.append(ss[row:row + height, current_col:current_col + width])
        for n in range(1, 3):
            self.sprites.insert(4, self.sprites[n])
