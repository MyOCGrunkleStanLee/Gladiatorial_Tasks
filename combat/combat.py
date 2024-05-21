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

    def change_phase(self, phase):
        """
        changes the phase of combat which will change what behaviors will be active in the combat scene
        phases of combat go as follows
        start: the default phase this phase is all the set-up like generating enemies
        select_attack: in this phase the player will select a move and the enemies will also automatically select a move (for now it's random)
        select_target: in this phase the player will select a valid target (all moves have enemies as valid targets r now) the enemies will do the same (also at random)
        process_attack: in this phase the combat engine will do math and update values on the emotions
        show_animation: this phase will show flashy colors based on moves later for now skip
        clean_up: this phase checks if a win or loss scenario has happened and does clean up (like removing dead enemies)
        end: ends combat and switches back to do_it_irl

        :param phase: the phase you want to switch combat to
        :return: None
        """
        self.phase = phase

    # todo we need to get the user to select a move for each of their emotions
    def select_attack(self):
        pass

    # todo have the user select a target to attack
    def select_valid_targets(self):
        pass

    # todo process the attack
    def process_attack(self, emotion):
        # todo program type advantages and disadvantages
        print(emotion.attack.power)
        attack = emotion.attack
        print(emotion.effectiveness)
        effectiveness = emotion.effectiveness
        print(emotion.target.resilience)
        target = emotion.target
        target.motivation -= math.ceil((attack.power * (1 + effectiveness / 100) * (attack.power / target.resilience)))

    # todo show animation
    def show_animation(self):
        pass

    # todo have enemy select an attack and target
    def select_enemy_attack(self, enemy):
        enemy.attack = random.choice(enemy.learned_moves)

    def select_enemy_target(self, enemy, targets: list):
        enemy.target = random.choice(targets)

    def clean_emotion(self, emotion):
        self.emotions.remove(emotion)

    def clean_enemies(self, enemy):
        self.enemies.remove(enemy)

    # todo inform the player of the outcome
    def display_combat_info(self):
        pass
