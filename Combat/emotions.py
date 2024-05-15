# todo create a framework of what emotions will look like

"""
stats:
    motivation (hp)
    effectiveness? (attack)
    resilience (defense)
    typing
"""


class Emotion:
    def __init__(self):
        self.name = ""
        self.motivation = 0
        self.effectiveness = 0
        self.resilience = 0
        self.typing = ""
        self.level = 1
        self.experience_factor = 0
        self.learnable_moves = []

    def initialize_emotion(self, name, motivation, effectiveness, resilience, typing, experience_factor, learnable_moves):
        """
        this will be used for each emotions basic starting stats at the start of the game launch
        :param name: the name of the character
        :param motivation: the HP stat of the character
        :param effectiveness: the ATT stat of the character
        :param resilience:  the DEF stat of the character
        :param typing: The Element of the character
        :param experience_factor: rate at which experience is needed to lvl up
        :param learnable_moves: a list of the moves that emotion will have
        :return: None
        """
        self.name = name
        self.motivation = motivation
        self.effectiveness = effectiveness
        self.resilience = resilience
        self.typing = typing
        self.experience_factor = experience_factor
        self.learnable_moves = learnable_moves


# anger
# example of what an initialized emotion will look like
anger = Emotion()
anger.initialize_emotion("Anger", 30, 50, 10, "anger", 1,
                         [])

# embarrassment


# calmness


# stress


# optimism



