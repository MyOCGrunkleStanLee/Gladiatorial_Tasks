import pygame
from combat.player import PlayerEmotion
from combat.enemies import EnemyEmotion
from start.button import Button


class CombatUI:
    def __init__(self, display, current_phase):
        # get the player and enemy from list from somewhere else
        self.player = PlayerEmotion("Happiness", "Assets/LargeGoldSquare.png", display)
        self.enemy = EnemyEmotion("Frustration", "Assets/LargeGoldSquare.png")
        self.display = display
        self.current_phase = current_phase


    def update(self):
        match self.current_phase:
            case "idle":
                self.draw_idle()
            case "select_attack":
                # TODO draw attack menu, 4 buttons
                self.draw_attack_menu()
            case "select_target":
                # TODO put button on enemy
                pass
            case "process_attack":
                # TODO make attack button clickable
                pass
            case "show_animation":
                # TODO animate
                pass
        return self.current_phase


    def draw_idle(self):
        # activate the player button
        self.player.button_activated = True
        if self.player.button.activated:
            # change state, open menu
            self.current_phase = "select_attack"
        
        # draw player and enemy
        self.player.draw(self.display)
        self.enemy.draw(self.display)
        


    def draw_attack_menu(self):
        # overlay
        self.image = pygame.image.load("Assets/")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.display.blit(self.image, self.rect)

        # attack choose 4 buttons
        

        # w, h = pygame.display.get_surface().get_size()
        # rect = pygame.Rect(w//2-200, 350, 400, 200)
        # pygame.draw.rect(self.display, (255, 255, 255), rect, 0, 4)
        # pygame.draw.rect(self.display, (0, 0, 0), rect, 4, 4)


        # self.font = pygame.font.SysFont("College", 30)
        # # menu
        # cols, rows = 2,2
        # for col in range(cols):
        #     for row in range(rows):
        #         x = rect.left + rect.width / 4 + (rect.width / 2) * col
        #         y = rect.top + rect.height / 4 + (rect.height / 2) * row
        #         i = col + 2 * row

        #         text_surf = self.font.render("hello", True, 'black')
        #         text_rect = text_surf.get_rect(center = (x,y))
        #         self.display.blit(text_surf, text_rect)
