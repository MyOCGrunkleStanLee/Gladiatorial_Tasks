# todo create a framework of what emotions will look like

"""
stats:
    motivation (hp)
    effectiveness? (attack)
    resilience (defense)
    typing
"""
import pygame
from combat.emotions import Emotion


class PlayerEmotion(Emotion):
    def __init__(self, name, image_path):
        super().__init__(name, image_path)
        self.learnable_moves = []


    def teach_move(self, move: object):
        self.learned_moves.append(move)


    def forget_move(self, move: object):
        if move not in self.learned_moves:
            raise "Move not in learned moves!"
        self.learned_moves.remove(move)


    def draw(self, display):
        image = pygame.image.load(self.image_path)
        w, h = pygame.display.get_surface().get_size()
        rect = image.get_rect(bottomleft=(200, h-50))
        display.blit(image, rect)


# anger
# example of what an initialized emotion will look like
anger = PlayerEmotion("Anger", "")
anger.initialize_emotion("Anger", 30, 50, 10, "anger", 1,
                         [], [])

# # happiness
happiness = PlayerEmotion("Happiness", "")
happiness.initialize_emotion("Happiness", 30, 50, 10, "joy", 1,
                              [], [])
# embarrassment


# calmness


# stress


# optimism



