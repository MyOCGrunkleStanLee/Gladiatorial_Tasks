# todo get the user to select a main task to do while playing the game
 
import pygame
from pygame.locals import MOUSEBUTTONDOWN
import sys
from start.button import Button
from utilities.game_state_object import GameStateObject
from utilities.generic_scene import GenericScene
from utilities.player_info import Player

class TaskScene(GenericScene):         

    def create_components(self):
        self.background_img = pygame.image.load("Assets/ExerciseTaskScreen.png").convert_alpha()
        
        # next task button
        next_button_image = pygame.image.load("Assets/NextButton.png").convert_alpha()
        self.next_button = Button(self.display, self.WIDTH//2, 450, next_button_image, 1)

        # overlay
        self.small_icon_golden = pygame.image.load("Assets/SmallGoldSquare.png").convert_alpha()
        self.big_icon_golden = pygame.image.load("Assets/LargeGoldSquare.png").convert_alpha()
        

    def game_body_loop(self):
        if self.next_button.activated:
            self.player_info.current_task += 1
            print("clicked")

        self.display.blit(self.background_img, (0, 0))
        self.next_button.draw(self.display)
        self.mark_finished_tasks()
        

    def mark_finished_tasks(self):
        # draw small overlays
        icon_x_coords = [254, 411, 579, 752, 951]
        y_coords = [280, 280, 280, 283, 283]
        for task, finished in self.player_info.tasks_state[self.player_info.current_project].items():
            if finished:
                # calculate x y
                x = icon_x_coords[task-1]
                y = y_coords[task-1]
                rect = self.small_icon_golden.get_rect(topleft=(x, y))
                self.display.blit(self.small_icon_golden, rect)

        # draw big overlay only if tasks are done
        icon_x_coord = 1144
        y_coord = 259
        finished_projects = self.player_info.get_finished_projects()
        if self.player_info.current_project in finished_projects:
            x = icon_x_coord
            y = y_coord
            rect = self.big_icon_golden.get_rect(topleft=(x, y))
            self.display.blit(self.big_icon_golden, rect)