from sprite import Sprite
import cv2


# deprecated
class SpritePlayer(Sprite):
    sprites = []

    def __init__(self, head_row, body_row):
        super().__init__()

        for n in range(6):
            head = head_row.get_raw_list()[n]
            body = body_row.get_raw_list()[n]

            # create a roi
            rows, cols, channels = head.shape
            roi = body[0:rows, 0:cols]

            # create a mask
            head_gray = cv2.cvtColor(head, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(head_gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            # black-out area of head in roi
            body_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

            # take head from head image
            head_fg = cv2.bitwise_and(head, head, mask=mask)

            # put head in roi and modify main image
            dst = cv2.add(body_bg, head_fg)
            self.sprites.append(dst)
