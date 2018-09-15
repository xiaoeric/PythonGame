from abc import ABC


class State(ABC):
    def __init__(self, state, state_names={}):
        self.state = state
        self.state_names = state_names

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    # TODO: refactor state comparisons to one method

    def get_name(self):
        return self.state_names.get(self.state, 'Invalid state')


class GameState(State):
    INVASION = 0
    VICTORY = 1
    SHOP = 2

    def __init__(self, state):
        state_names = {
            self.INVASION: 'Invasion',
            self.VICTORY: 'Victory',
            self.SHOP: 'Shop'
        }
        super().__init__(state, state_names)


class ScreenState(State):
    NONE = 10
    FADE_IN = 11
    FADE_OUT = 12

    def __init__(self, state):
        state_names = {
            self.NONE: 'No effect',
            self.FADE_IN: 'Fading in...',
            self.FADE_OUT: 'Fading out...'
        }
        super().__init__(state, state_names)
