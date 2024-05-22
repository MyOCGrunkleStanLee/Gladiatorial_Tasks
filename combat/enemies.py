# todo design an enemy framework as well
# i am thinking that we can use the same framework we use for emotions and just add a tag
# or we could just create a new system for it
import os
import pygame
import combat.moves
from combat.emotions import Emotion
from start.button import Button


class EnemyEmotion(Emotion):
    def __init__(self, name, image_path):
        super().__init__(name, image_path)
        self.target = None
        self.attack = None
        self.enemy = True

        self.x, self.y = 800, 40

        self.image = pygame.image.load(self.image_path)
        self.button = Button(None, self.x, self.y, self.image, 1, positioning="topleft")

    def draw(self, display):
        # draws enemy as button
        self.button.draw(display)

        # healthbar
        healthbar_img = pygame.image.load("Assets/CombatCharacterStatBlock.png")
        ext = healthbar_img.get_rect()[2:4]
        scalar = 1.5
        healthbar_img = pygame.transform.scale(healthbar_img, (int(ext[0] * scalar), int(ext[1] * scalar)))
        self.healthbar_x, self.healthbar_y = self.x-200, self.y+60
        healthbar_rect = healthbar_img.get_rect(bottomleft=(self.healthbar_x, self.healthbar_y))

        # name
        font = pygame.font.SysFont(None, 30)
        name_surface = font.render(self.name, True, (255, 255, 255))
        text_rect = name_surface.get_rect(bottomleft=(self.healthbar_x+15, self.healthbar_y-60))
        



        #draw
        display.blit(healthbar_img, healthbar_rect)
        display.blit(name_surface, text_rect)
        self.update_health_bar(display)

    
    def update_health_bar(self, display):
        x = self.healthbar_x+123
        y = self.healthbar_y-28
        h = 8
        w = 98
        print(self.motivation)
        ratio = self.motivation / self.max_motivation  # assumed 100 to be max health
        pygame.draw.rect(display, (255, 0, 0), (x, y, w, h))
        pygame.draw.rect(display, (0, 255, 0), (x, y, w*ratio, h))
        

# frustration
Frustration = EnemyEmotion("Frustration", "Assets/Frustration.png")
Frustration.initialize_emotion("frustration", 20, 50, 3, 5, "anger",
                             5, [combat.moves.punch], [])
# procrastination
# distraction
# pain
# excuse
print(Frustration.resilience)
enemies = [Frustration]
