class Settings:

    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        self.player_speed_factor = 0.5

        self.animation_speed = 1.0 / 256

        # Dagger settings
        self.dagger_speed_factor = 0.75
        self.dagger_width = 15
        self.dagger_height = 3
        self.dagger_color = 60, 60, 60
        self.daggers_allowed = 3
