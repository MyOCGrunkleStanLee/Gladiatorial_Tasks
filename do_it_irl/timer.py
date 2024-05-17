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
        self.activated = False


    def update_timer(self):
        time_left = self.get_time_left()
        if time_left == 0:
            self.done = True
        return self.format_time(time_left)
        

    def get_time_left(self):
        current_time = pygame.time.get_ticks()
        time_passed = current_time - self.start_time
        return max(0, self.time_in_seconds - time_passed // 1000)
    

    def format_time(self, seconds) -> str:
        minutes = seconds // 60
        seconds = seconds % 60
        return "{:02}:{:02}".format(minutes, seconds)
    

    def render_string(self, str):
        return self.font.render(str, True, (0, 0, 0))
    

    def draw(self, display):
        # if activated update timer
        text = self.update_timer() if self.activated else \
            self.format_time(self.time_in_seconds)
        
        text_surface = self.render_string(text)
        rect = text_surface.get_rect(center=(self.x, self.y))
        display.blit(text_surface, rect)


    # start the timer
    def start(self):
        self.activated = True
        self.start_time = pygame.time.get_ticks()



"""
Example usage:
timer = Timer(5, (100, 100), 30)
timer.start()

# call in gameloop
timer.draw()
"""