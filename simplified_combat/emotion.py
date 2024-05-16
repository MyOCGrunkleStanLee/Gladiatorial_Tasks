from simplified_combat.move import Move

class Emotion:
    
    def __init__(self, name, health, moveset) -> None:
        self.name = name
        self.health = health
        self.moveset = moveset


    def targeted_by_move(self, move: Move) -> None:
        #hardcoded that moves only deal damage
        self.health -= move.damage_amount

        if self.health <= 0:
            # die? faint?
            pass