class GameStateObject:
    """
    This class is used store data about the current game state and shared across scenes
    """

    def __init__(self, current_state=None):
        self.current_state = current_state
        self.keydown_event = None
    
    #setters and getters unneccesary (just make everything public!)
