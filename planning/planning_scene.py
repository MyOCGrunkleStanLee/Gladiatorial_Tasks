import pygame
from utilities.generic_scene import GenericScene
from planning.input_box import InputBox


class PlanningScene(GenericScene):

    def create_components(self) -> None:
        self.prompt_list = [
            "How many Push Ups?",
            "How many sit ups?",
            "How many squats?",
            "How many seconds plank?",
            "How many pull-ups?",
        ]

        my_font = pygame.font.SysFont('College', 30)
        self.text_surface = my_font.render('Gladiatorial Tasks', False, (0, 0, 0))

        CENTERED_DIMENSIONS = (
            340, #x_position
            120, #y_position
            600, #width
            400, #length
        )  # These measurements create a centered rectangle for a screen WIDTH, HEIGHT = 1280, 620

        self.planning_input_box = InputBox(self.display, *CENTERED_DIMENSIONS)

    def game_body_loop(self) -> None:
        self.display.fill("blue")

        self.planning_input_box.draw()
