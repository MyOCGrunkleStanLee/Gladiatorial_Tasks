class Move:
    def __init__(self):
        self.name = "put the moves name here"
        self.description = "put your description here"
        self.power = 0
        self.special_effects = None

    def initialize_move(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power


# todo create moves
punch = Move()
punch.initialize_move("punch", "A basic attack", 10)

# todo map moves to emotions

