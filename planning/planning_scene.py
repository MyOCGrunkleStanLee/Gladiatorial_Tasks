import pygame
from utilities.generic_scene import GenericScene
from planning.input_box import InputBox
from start.button import Button


class PlanningScene(GenericScene):

    def create_components(self) -> None:
        self.background_img = pygame.image.load(
            "Assets/BreakItDownScreen.png"
        ).convert_alpha()

        self.selected_tasks = []

        # selectable tasks as strings
        self.task_strings = [
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

        # (x, y) coordinate tules based on topleft positioning
        task_positions = [
            (615, 75),
            (615, 155),
            (615, 225),
            (615, 305),
            (615, 388),
            (615, 465),
            (940, 75),
            (940, 155),
            (940, 225),
            (940, 305),
            (940, 388),
            (940, 465),
        ]

        self.bordered_task = pygame.image.load(
            "planning/border_task.png"
        ).convert_alpha()

        self.task_buttons = []
        for x_position, y_position in task_positions:
            created_button = Button(
                self.display, x_position, y_position, self.bordered_task, 1, "topleft"
            )
            self.task_buttons.append(created_button)

    def game_body_loop(self) -> None:

        for index, button in enumerate(self.task_buttons):
            if button.activated:
                self.queue_task(index)
                print(self.selected_tasks)

        self.display.blit(self.background_img, (0, 0))
        for button in self.task_buttons:
            button.draw()

    def next_screen(self) -> None:
        self.player_info.selected_tasks = self.selected_tasks
        self.game_state_object.current_state = "select_starter"

    def queue_task(self, task_index):
        if self.task_strings[task_index] == '':
            return

        self.selected_tasks.append(self.task_strings[task_index])
        self.task_strings[task_index] = ''

        # Hardcoded limit based on BreakItDown.png
        if len(self.selected_tasks) == 5:
            self.next_screen()
            return