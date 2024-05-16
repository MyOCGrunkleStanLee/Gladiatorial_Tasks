import random
import enemies

def randomly_select_enemy():
    return random.choice(enemies.enemies)


class Combat:
    # todo program type advantages and disadvantages
    type_advantage = {}

    def __init__(self, Player: object):
        """
        To initialize combat an enemy and player need to be input
        :param Player: the player class type object
        """
        self.emotions = Player.emotions
        self.enemies = []

    def generate_enemies(self, number: int = 1, opponents: list = None):
        if opponents is None:
            opponents = []

        for enemy in opponents:
            self.enemies.append(enemy)

        for i in range(len(opponents) - number):
            self.enemies.append(randomly_select_enemy())

    # todo we need to get the user to select a move for each of their emotions
    def select_attack(self):
        pass

    # todo have the user select a target to attack
    def select_valid_targets(self):
        pass

    # todo process the attack
    def process_attack(self):
        # todo program type advantages and disadvantages
        pass

    # todo show animation
    def show_animation(self):
        pass

    # todo have enemy select an attack and target
    def select_enemy_attack(self):
        pass

    def select_enemy_target(self):
        pass

    # todo inform the player of the outcome
    def display_combat_info(self):
        pass
