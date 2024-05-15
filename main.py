# todo initialize program
# todo get user controls set up

import pygame
import sys

from game_state_manager import GameStateManager
from GameStart.start_task import TaskTree
from Tasks.exercise import Exercise

# final vars
WIDTH, HEIGHT = 1280, 620
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # handles different state
        self.gameStateManager = GameStateManager("task_tree")
        # instances of our states
        self.task_tree_state = TaskTree(self.screen, self.gameStateManager)
        self.exercise_state = Exercise(self.screen, self.gameStateManager)
        # dict of all possible state
        self.states = {"task_tree": self.task_tree_state, "exercise": self.exercise_state}

    def run(self):
        # this is the main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # this allows to switch between states
            self.states[self.gameStateManager.get_state()].run()
            
        
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()