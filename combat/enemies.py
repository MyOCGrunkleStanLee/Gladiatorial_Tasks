# todo design an enemy framework as well
# i am thinking that we can use the same framework we use for emotions and just add a tag
# or we could just create a new system for it

import pygame
import combat.moves
from combat.emotions import Emotion


class EnemyEmotion(Emotion):
    def __init__(self, name, image_path):
        super().__init__(name, image_path)
        self.target = None
        self.attack = None

    
    def draw(self, display):
        image = pygame.image.load(self.image_path)
        w, h = pygame.display.get_surface().get_size()
        rect = image.get_rect(topleft=(w-400, 0))
        display.blit(image, rect)


# frustration
Frustration = EnemyEmotion("Frustration", "")
Frustration.initialize_emotion("frustration", 10, 50, 3, "anger",
                             5, [combat.moves.punch], [])
# procrastination
# distraction
# pain
# excuse
enemies = [Frustration]
