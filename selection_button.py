class SelectionButton:
    def __init__(self, surface, action=None):
        self.surface = surface
        self.action = action

    def get_surface(self):
        return self.surface

    def select(self):
        if self.action is not None:
            self.action()
