class SelectionButton:
    def __init__(self, surface, ai_settings, action=None, text=None):
        self.surface = surface
        self.ai_settings = ai_settings
        self.action = action
        self.text = text
        self.text_surf = None

    def get_surface(self):
        return self.surface

    def select(self):
        if self.action is not None:
            self.action()

    def render_text(self, screen, coords):
        if self.text is not None:
            self.text_surf = self.ai_settings.font.render(self.text, False, (0, 0, 0))
            text_half_width = self.text_surf.get_width() / 2.0
            text_half_height = self.text_surf.get_height() / 2.0
            surf_half_width = self.surface.get_width() / 2.0
            surf_half_height = self.surface.get_height() / 2.0
            x = surf_half_width - text_half_width
            y = surf_half_height - text_half_height
            screen.blit(self.text_surf, (x + coords[0], y + coords[1]))
