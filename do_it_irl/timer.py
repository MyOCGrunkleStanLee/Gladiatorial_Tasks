import pygame
from utilities.generic_scene import GenericScene

class Timer(GenericScene):

    def __init__(self, time_in_seconds, position, fontsize, font=None):
        self.time_in_seconds = time_in_seconds
        self.x = position[0]
        self.y = position[1]
        self.font = pygame.font.Font(font, fontsize) 
        self.start_time = 0
        self.done = False

    def update(self):
        current_time = pygame.time.get_ticks()
        time_passed = current_time - self.start_time
        time_left = max(0, self.time_in_seconds - time_passed // 1000)

        if time_left == 0:
            self.done = True

        minutes = time_left // 60
        seconds = time_left % 60
        time_str = "{:02}:{:02}".format(minutes, seconds)

        # Render the text
        return self.font.render(time_str, True, (0, 0, 0))

    def draw(self, display):
        text = self.update()
        display.blit(text, (self.x, self.y))

    # start the timer
    def start(self):
        self.start_time = pygame.time.get_ticks()

"""
Example usage:
timer = Timer(5, (100, 100), 30)
timer.start()

# call in gameloop
timer.draw()
"""