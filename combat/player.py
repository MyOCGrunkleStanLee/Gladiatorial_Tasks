# todo create a framework of what emotions will look like
import combat.moves
import pygame
from combat.emotions import Emotion
from start.button import Button

"""
stats:
    motivation (hp)
    effectiveness (attack)
    resilience (defense)
    typing
"""

class PlayerEmotion(Emotion):
    def __init__(self, name, image_path):
        super().__init__(name, image_path)
        self.learnable_moves = []
        self.target = None
        self.attack = None
        self.enemy = False

        self.image = pygame.image.load(self.image_path)
        self.button = Button(None, 230, 550, self.image, 1, positioning="bottomleft")


    def teach_move(self, move: object):
        self.learned_moves.append(move)


    def forget_move(self, move: object):
        if move not in self.learned_moves:
            raise "Move not in learned moves!"
        self.learned_moves.remove(move)


    def draw(self, display):
        # this method either draws normal sprite or button
        self.button.draw(display)


# anger
# example of what an initialized emotion will look like
anger = PlayerEmotion("Anger", "Assets/AngerBull.png")
anger.initialize_emotion("Anger", 30, 50, 10, 7, "anger", 1,
                        [combat.moves.punch, combat.moves.heal, combat.moves.idk, combat.moves.something],
                         [])

# # # happiness
happiness = PlayerEmotion("Happiness", "Assets/HappyDog.png")
happiness.initialize_emotion("Happiness", 30, 30, 10, 3, "joy", 1,
                              [combat.moves.punch, combat.moves.heal, combat.moves.idk, combat.moves.something],
                             [])
# embarrassment


# calmness


# stress


# optimism



