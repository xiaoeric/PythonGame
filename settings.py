class Settings:

    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        self.player_speed_factor = 2.5

        self.animation_speed = 1.0 / 10.0

        # Dagger settings
        self.dagger_speed_factor = 9
        self.dagger_width = 15
        self.dagger_height = 3
        self.dagger_color = 60, 60, 60
        self.daggers_allowed = 3

        # Faceless settings
        self.faceless_speed_factor = 1
        self.horde_crawl_speed = 0.5
        # horde direction of 1 represents down; -1 represents up
        self.horde_direction = 1
