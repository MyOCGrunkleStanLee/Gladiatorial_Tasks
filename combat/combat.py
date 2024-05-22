import random
import combat.enemies
import math

def randomly_select_enemy():
    print(combat.enemies.enemies)
    return random.choice(combat.enemies.enemies)


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
        self.phase = "start"

    def generate_enemies(self, number: int = 1, opponents: list = None):
        if opponents is None:
            opponents = []

        for enemy in opponents:
            self.enemies.append(enemy)

        for i in range(number - len(opponents)):
            self.enemies.append(randomly_select_enemy())

    # todo process the attack
    def process_attack(self, emotion):
        print("PROCESSING AN ATTACK")
        # todo program type advantages and disadvantages
        attack = emotion.attack
        effectiveness = emotion.effectiveness
        target = emotion.target
        target.motivation -= math.ceil((attack.power * 1 + ((effectiveness / target.resilience) / 100)))

    # todo show animation
    def show_animation(self):
        pass

    # todo have enemy select an attack and target
    def select_enemy_attack(self, enemy):
        enemy.attack = random.choice(enemy.learned_moves)

    def select_enemy_target(self, enemy, targets: list):
        enemy.target = random.choice(targets)

    # todo inform the player of the outcome
    def display_combat_info(self):
        print(self.enemies)
        print("Enemies stats:")
        for enemy in self.enemies:
            print(f"name: {enemy.name}")
            print(f"Motivation: {enemy.motivation}")
            print(f"Effectiveness: {enemy.effectiveness}")
            print(f"Speed: {enemy.speed}")
        print("Player Emotions Stats:")
        for emotion in self.emotions:
            print(f"name: {emotion.name}")
            print(f"Motivation: {emotion.motivation}")
            print(f"Effectiveness: {emotion.effectiveness}")
            print(f"Speed: {emotion.speed}")

