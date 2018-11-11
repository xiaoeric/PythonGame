import pygame
from game_state import ScreenState as ScS
from selection_button import SelectionButton as Selection


class ShopMenu:
    def __init__(self, screen_state, ai_settings):
        menu_filename = 'images/3DS - Fire Emblem Fates - Support Conversation Text Boxes.png'
        self.menu_source = pygame.image.load(menu_filename)
        self.selections = []
        self.current_selection = 0

        self.create_selection(ai_settings, text='Test 1')
        self.create_selection(ai_settings, text='Test 2')

        # exits shop and returns to invasion
        self.create_selection(ai_settings, action=lambda: screen_state.set_state(ScS.FADE_OUT), text='Continue')

        selection_arrow = self.menu_source.subsurface(pygame.Rect(315, 176, 16, 16))
        self.selection_arrow = pygame.transform.rotate(selection_arrow, 90)

    def create_selection(self, ai_settings, action=None, text=None):
        """Creates a new selection box in the menu"""
        rect = pygame.Rect(2, 176, 197, 56)
        surface = self.menu_source.subsurface(rect)
        selection = Selection(surface, ai_settings, action, text)
        self.selections.append(selection)
        return selection

    def update_selection(self):
        """Moves to the next selection in the menu forwards"""
        self.current_selection = (self.current_selection + 1) % len(self.selections)

    def update_selection_rev(self):
        """Moves to the next selection in the menu backwards"""
        if self.current_selection > 0:
            self.current_selection -= 1
        else:
            self.current_selection = len(self.selections) - 1

    def get_selections(self):
        """Returns array of selections"""
        return self.selections

    def get_current_selection(self):
        """Returns the current selection"""
        return self.current_selection

    def update_screen(self, screen):
        """Updates the menu on the screen"""
        x = 350
        y = 50
        for n in range(len(self.selections)):
            screen.blit(self.selections[n].get_surface(), (x, y))
            self.selections[n].render_text(screen, (x, y))
            if self.current_selection == n:
                arrow_rect = self.selection_arrow.get_rect()
                button_rect = self.selections[n].get_surface().get_rect()
                screen.blit(self.selection_arrow, (x - arrow_rect.width, y + button_rect.height / 2
                                                   - arrow_rect.height / 2))
            y += self.selections[n].get_surface().get_size()[1]
