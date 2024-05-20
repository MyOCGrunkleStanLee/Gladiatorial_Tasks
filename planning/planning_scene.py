import pygame
from utilities.generic_scene import GenericScene
from planning.input_box import InputBox
from start.button import Button


class PlanningScene(GenericScene):

    def create_components(self) -> None:
        self.background_img = pygame.image.load(
            "Assets/BreakItDownScreen.png"
        ).convert_alpha()

        task_strings = [
            '10 Push Ups',
            '10 Pull Ups',
            '1-Minute Plank',
            '10 Sit Ups',
            '10 Squats',
            '10 Crunches',
            '10 Lunges',
            '20 High Knees',
            '10 Incline Rows',
            '10 Calf Raises',
            '10 Jumping Jacks',
            '10 Burpees',
        ]

        task_positions = []

        self.bordered_task = pygame.image.load("planning/border_task.png").convert_alpha()
        self.push_up_button = Button(
            self.display, 616, 76, self.bordered_task, 1, "topleft"
        )

    def game_body_loop(self) -> None:

        self.display.blit(self.background_img, (0, 0))
        self.push_up_button.draw()

    def next_screen(self) -> None:
        self.game_state_object.current_state = "select_starter"
