# todo design an enemy framework as well
# i am thinking that we can use the same framework we use for emotions and just add a tag
# or we could just create a new system for it
import moves
class Enemy:
    def __init__(self):
        self.name = ""
        self.motivation = 0
        self.effectiveness = 0
        self.resilience = 0
        self.typing = ""
        self.level = 1
        self.learned_moves = []
        self.experience_value = 0

    def initialize_enemy(self, name, motivation, effectiveness, resilience, typing, experience_value, learned_moves):
        """
        this will be used for each emotions basic starting stats at the start of the game launch
        :param name: the name of the character
        :param motivation: the HP stat of the character
        :param effectiveness: the ATT stat of the character
        :param resilience:  the DEF stat of the character
        :param typing: The Element of the character
        :param experience_value: rate at which experience is dropped when defeated
        :param learned_moves: any moves you want the character to start with
        :return: None
        """
        self.name = name
        self.motivation = motivation
        self.effectiveness = effectiveness
        self.resilience = resilience
        self.typing = typing
        self.experience_value = experience_value
        self.learned_moves = learned_moves


# frustration
frustration = Enemy()
frustration.initialize_enemy("frustration", 10, 50, 3, "anger",
                             5, moves.punch)
# procrastination
# distraction
# pain
# excuse
enemies = [frustration]