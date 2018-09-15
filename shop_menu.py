import pygame


class ShopMenu:
    def __init__(self):
        menu_filename = 'images/3DS - Fire Emblem Fates - Support Conversation Text Boxes.png'
        self.menu_source = pygame.image.load(menu_filename)
        self.selections = [None]
        self.current_selection = None

        self.continue_button = self.create_selection()
        self.create_selection()

        selection_arrow = self.menu_source.subsurface(pygame.Rect(315, 176, 16, 16))
        self.selection_arrow = pygame.transform.rotate(selection_arrow, 90)

    def create_selection(self):
        rect = pygame.Rect(2, 176, 197, 56)
        surface = self.menu_source.subsurface(rect)
        self.selections.insert(1, surface)
        return surface

    # def update_selection(self):

    def update_screen(self, screen):
        x = 350
        y = 50
        for n in range(len(self.selections)):
            if self.selections[n] is not None:
                screen.blit(self.selections[n], (x, y))
                y += self.selections[n].get_size()[1]
