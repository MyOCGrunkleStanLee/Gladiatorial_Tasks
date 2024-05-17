class Player:
    def __init__(self):
        self.player_name = "person"
        self.emotions = []
        
        # to keep track at which task the player is
        # increment after each combat
        # should prob be int?
        self.task = "task1"

    def add_emotion(self, emotion: object):
        self.emotions.append(emotion)
