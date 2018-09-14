INVASION = 0
VICTORY = 1
SHOP = 2
FADE_IN = 3
FADE_OUT = 4


class GameState:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_name(self):
        if self.state == INVASION:
            return 'Invasion'
        elif self.state == VICTORY:
            return 'Victory'
        elif self.state == SHOP:
            return 'Shop'
        elif self.state == FADE_IN:
            return 'Fading in...'
        elif self.state == FADE_OUT:
            return 'Fading out...'
