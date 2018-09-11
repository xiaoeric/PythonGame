INVASION = 0
VICTORY = 1
SHOP = 2


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
