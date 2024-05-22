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

    def process_effects(self, emotion):
        base_stat_map = {"health": emotion.max_motivation, "attack": emotion.base_effectiveness,
                         "defense": emotion.base_resilience, "speed": emotion.base_speed}

        for effect in emotion.active_effects:
            if effect.timer_handler() is True:
                print("EFFECT RAN OUT OF TIME")
                # when the timer runs out we make their base stat back to what it was
                emotion.change_stat(effect.affected_stat, base_stat_map.get(effect.affected_stat))
                emotion.active_effects.remove(effect)
                return
            # change the stat value the effect affects by the amount it affects it by

            value = effect.apply_effect(base_stat_map.get(effect.affected_stat))
            emotion.change_stat(effect.affected_stat, value)

    def process_attack(self, emotion):
        print("PROCESSING AN ATTACK")
        if emotion.attack.special_effects:
            print("ATTACK HAD A SPECIAL EFFECT APPLYING IT NOW...")
            for special_effect in emotion.attack.special_effects:
                if special_effect.affected_stat == "health":
                    emotion.motivation += special_effect.power
                    if emotion.motivation > emotion.max_motivation:
                        emotion.motivation = emotion.max_motivation

                    print(f"Healed {emotion.name} by {special_effect.power}")
                    return

                if emotion.attack.target == "self":
                    emotion.active_effects.append(special_effect)

                else:
                    emotion.target.active_effects.append(special_effect)
            print(f"SPECIAL EFFECTS HAVE BEEN APPLIED EMOTIONS EFFECTS ARE CURRENTLY {emotion.active_effects}")

        # todo program type advantages and disadvantages
        attack = emotion.attack
        effectiveness = emotion.effectiveness
        target = emotion.target
        target.motivation -= math.ceil((attack.power * 1 + ((effectiveness / target.resilience) / 100)))

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

