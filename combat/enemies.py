# todo design an enemy framework as well
# i am thinking that we can use the same framework we use for emotions and just add a tag
# or we could just create a new system for it
import os
import pygame
import combat.moves
from combat.emotions import Emotion
from start.button import Button


class EnemyEmotion(Emotion):
    def __init__(self, name, image_path, display=None):
        super().__init__(name, image_path)
        self.target = None
        self.attack = None

        self.image = pygame.image.load(self.image_path)
        self.button = Button(display, 800,40, self.image, 1, positioning="topleft")

    def draw(self, display):
        # draws enemy as button
        self.button.draw()
        

# frustration
Frustration = EnemyEmotion("Frustration", "Assets\LargeGoldSquare.png", None)
Frustration.initialize_emotion("frustration", 10, 50, 3, "anger",
                             5, [combat.moves.punch], [])
# procrastination
# distraction
# pain
# excuse
print(Frustration.resilience)
enemies = [Frustration]
