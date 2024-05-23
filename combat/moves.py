from combat.effect import Effect
class Move:
    def __init__(self):
        self.name = "put the moves name here"
        self.description = "put your description here"
        self.target = "enemy"
        self.power = 0
        self.effect_power = 0
        self.special_effects = []
        self.move_timer = 0

    def initialize_move(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power


# todo create moves
punch = Move()
punch.initialize_move("Punch", "A basic attack", 10)

heal = Move()
heal.initialize_move("Heal", "heals target", 0)
heal.target = "self"
heal.special_effects.append(Effect("Heal", 10, 0, "health"))

clarity = Move()
clarity.initialize_move("Clarity", "buffs user attack by 50% for 3 turns", 0)
clarity.special_effects.append(Effect("Clarity", 150, 4, "attack"))
clarity.target = "self"

gaslight = Move()
gaslight.initialize_move("Gaslight", "debuffs targets attack by 50% for 3 turns", 0)
gaslight.special_effects.append(Effect("Gaslight", 50, 4, "attack"))
