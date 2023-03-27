from levelup.controller import GameController


class GameControllerLibrary:
    def initialize_controller(self):
        self.controller = GameController()

    def create_character_with_name(self, charactername):
        self.controller.create_character(charactername)

    def character_name_should_be(self, expected):
        if self.controller.character.name != expected:
            raise AssertionError(
                f"{self.controller.character.name} != {expected}"
            )

    def number_of_map_positions_should_be(self, expected):
        pass  # Not implemented

    def starting_X_coordinate_should_be(self, expected):
        pass  # Not implemented

    def starting_Y_coordinate_should_be(self, expected):
        pass  # Not implemented

    def starting_move_count_should_be(self, expected):
        pass  # Not implemented
