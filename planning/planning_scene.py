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

        self.input_box = InputBox(self.display, *CENTERED_DIMENSIONS, self.prompt_list[0])

    def game_body_loop(self) -> None:
        self.display.fill("blue")

        keydown_event = self.game_state_object.keydown_event

        if keydown_event != None:
            if keydown_event.key == pygame.K_BACKSPACE:
                self.input_box.user_text = self.input_box.user_text[:-1]
            else:
                self.input_box.user_text += keydown_event.unicode

            self.game_state_object.keydown_event = None
            

        self.input_box.draw()
    
    def next_screen(self) -> None:
        self.game_state_object.current_state = "select_starter"
