import pygame


class Sprite:
    def __init__(self, sprites=[], alpha_masks=[]):
        self.sprites = sprites
        self.alpha_masks = alpha_masks

    @classmethod
    def from_coord(cls, col, row, width, height, gap, filename):
        sprites = []
        alpha_masks = []
        ss = pygame.image.load(filename)
        for n in range(4):
            current_col = (col + n * (width + gap))
            rect = pygame.Rect(current_col, row, width, height)
            sprites.append(ss.subsurface(rect))

            rect_alpha = pygame.Rect(current_col + 128, row, width, height)
            alpha_masks.append(ss.subsurface(rect_alpha))
        for n in range(1, 3):
            sprites.insert(4, sprites[n])
            alpha_masks.insert(4, alpha_masks[n])

        return cls(sprites, alpha_masks)

    @classmethod
    def from_merge(cls, head_row, body_row):
        sprites = []
        for n in range(len(body_row.get_list())):
            # TODO: get head and body sprites to layer properly
            # layering should occur as follows:
            # > body top
            # > head top
            # > body bottom
            # > head bottom
            head = head_row.get_list()[n]
            body = body_row.get_list()[n]
            body_alpha = body_row.get_alpha_masks()[n]
            body.blit(head, (6, 1))
            body_top = cls.get_top(body, body_alpha)
            body.blit(body_top, (0, 0))
            # TODO: figure out where her head goes
            # her left eye goes on the same column as the brooch on her chest
            # her chin ends right above that brooch
            sprites.append(body)

        return cls(sprites)

    def get_list(self):
        return self.sprites

    def get_alpha_masks(self):
        return self.alpha_masks

    @staticmethod
    def get_top(sprite, alpha_mask):
        if sprite.get_size() != alpha_mask.get_size():
            raise ValueError('Sprite and alpha mask are not the same size!')

        blank = pygame.Surface(sprite.get_size(), flags=pygame.SRCALPHA)
        top_pxarr = pygame.PixelArray(blank)
        sprite_pxarr = pygame.PixelArray(sprite)
        alpha_mask_pxarr = pygame.PixelArray(alpha_mask)

        for x in range(sprite_pxarr.shape[0]):
            for y in range(sprite_pxarr.shape[1]):
                if alpha_mask_pxarr[x, y] == alpha_mask.map_rgb((136, 136, 136)):
                    top_pxarr[x, y] = sprite_pxarr[x, y]

        top = top_pxarr.make_surface()
        return top
