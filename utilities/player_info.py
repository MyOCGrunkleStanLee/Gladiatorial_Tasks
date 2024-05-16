class Player:
    def __init__(self):
        self.player_name = "person"
        self.emotions = []

    def add_emotion(self, emotion: object):
        self.emotions.append(emotion)
