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
            rect = pygame.Rect(current_col, row, width + 1, height + 1)
            sprites.append(ss.subsurface(rect))

            rect_alpha = pygame.Rect(current_col + 128, row, width + 1, height + 1)
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

            # getting pair of head and body
            head = head_row.get_list()[n]
            body = body_row.get_list()[n]

            # creating blank surface to blit head and body layers
            sprite = pygame.Surface(body.get_size(), pygame.SRCALPHA)

            body_alpha = body_row.get_alpha_masks()[n]
            body_top = cls.get_top(body, body_alpha)
            head_alpha = head_row.get_alpha_masks()[n]
            head_top = cls.get_top(head, head_alpha)

            head_pos = (6, 1)

            sprite.blit(head, head_pos)
            sprite.blit(body, (0, 0))
            sprite.blit(head_top, head_pos)
            sprite.blit(body_top, (0, 0))
            # TODO: figure out where her head goes
            # her left eye goes on the same column as the brooch on her chest
            # her chin ends right above that brooch
            sprites.append(sprite)

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
