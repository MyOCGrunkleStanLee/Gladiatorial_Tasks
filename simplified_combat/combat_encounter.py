from simplified_combat.emotion import Emotion
from simplified_combat.move import Move

class CombatEncounter:
    
    def __init__(self, player_party: list[Emotion], enemy_party: list[Emotion]) -> None:
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.current_turn: str = "player"

    def get_player_move_options(self) -> list[Move]:
        #hardcoded to assume player party is one emotion
        return self.player_party[0].moveset
    
    def get_enemy_move_options(self) -> list[Move]:
        return self.enemy_party[0].moveset
    
    def attack_player(self, move: Move) -> None:
        #hardcoded to attack first character in player party
        self.player_party[0].targeted_by_move(move)

    def attack_player(self, move: Move) -> None:
        #hardcoded to attack first character in enemy party
        self.enemy_party[0].targeted_by_move(move)