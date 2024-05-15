# todo create a framework for a move will look like
class Move:
    def __init__(self):
        self.description = "put your description here"
        self.power = 0
        self.special_effects = None

    def initialize_move(self, description, power):
        self.description = description
        self.power = power


# todo create moves
punch = Move()
punch.initialize_move("A basic attack", 10)

# todo map moves to emotions

