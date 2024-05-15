class Exercise:
    """
    This is our first demo task
    """
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        # paints screen blue
        self.display.fill("blue")

