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
from start.button import Button


class PlayerEmotion(Emotion):
    def __init__(self, name, image_path, display):
        super().__init__(name, image_path)
        self.learnable_moves = []
        #w, h = pygame.display.get_surface().get_size()
        self.x = 200
        self.y = 300
        self.button_activated = False
        self.button = None

        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        self.button = Button(display, self.x, self.y, self.image, 1, positioning="bottomleft")


    def teach_move(self, move: object):
        self.learned_moves.append(move)


    def forget_move(self, move: object):
        if move not in self.learned_moves:
            raise "Move not in learned moves!"
        self.learned_moves.remove(move)


    def draw(self, display):
        # this method either draws normal sprite or button
        if self.button_activated:
            self.button.draw()
        else:
           display.blit(self.image, self.rect)
        


# anger
# example of what an initialized emotion will look like
# anger = PlayerEmotion("Anger", "")
# anger.initialize_emotion("Anger", 30, 50, 10, "anger", 1,
#                          [], [])

# # # happiness
# happiness = PlayerEmotion("Happiness", "")
# happiness.initialize_emotion("Happiness", 30, 50, 10, "joy", 1,
#                               [], [])
# embarrassment


# calmness


# stress


# optimism



