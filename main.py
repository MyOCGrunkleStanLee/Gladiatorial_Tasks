import pygame
import sys
from utilities.generic_scene import GenericScene
from start.start_scene import StartScene
from GameStart.select_starter import SelectStarterScene
from planning.planning_scene import PlanningScene
from combat.combat_scene import CombatScene
from do_it_irl.do_it_irl_scene import DoItIRLScene
from utilities.game_state_object import GameStateObject
from utilities.player_info import Player

# final vars
WIDTH, HEIGHT = 1280, 620
FPS = 60


def start_game():
    pygame.init()

    pygame.display.set_caption("Gladitorial Tasks")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_state = GameStateObject(None)
    player_info = Player()

    scenes: dict[str, GenericScene] = {
        "start": StartScene(screen, game_state),
        "select_starter": SelectStarterScene(screen, game_state, player_info),
        "planning": PlanningScene(screen, game_state),
        "combat": CombatScene(screen, game_state, player_info),
        "do_it_irl": DoItIRLScene(screen, game_state, player_info),
    }
    game_state.current_state = "start"
    

    # this is the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # this allows to switch between states
        # todo when scenes switch if button is in same position it gets clicked instantly when you click the first one
        scenes[game_state.current_state].game_body_loop()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_game()

