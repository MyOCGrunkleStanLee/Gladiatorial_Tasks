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

        self.x, self.y = 230, 550

        self.image = pygame.image.load(self.image_path)
        self.button = Button(None, 230, 550, self.image, 1, positioning="bottomleft")


    def teach_move(self, move: object):
        self.learned_moves.append(move)


    def forget_move(self, move: object):
        if move not in self.learned_moves:
            raise "Move not in learned moves!"
        self.learned_moves.remove(move)


    def draw(self, display):
        self.button.draw(display)

        # healthbar
        healthbar_img = pygame.image.load("Assets/CombatCharacterStatBlock.png")
        ext = healthbar_img.get_rect()[2:4]
        scalar = 1.5
        healthbar_img = pygame.transform.scale(healthbar_img, (int(ext[0] * scalar), int(ext[1] * scalar)))
        self.healthbar_x, self.healthbar_y = self.x+250, self.y-60
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



