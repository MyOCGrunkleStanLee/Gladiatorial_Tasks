


class GameStateManager:
    """
    This class is used to switch between different states like startmenu, level1, level2...
    """
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state