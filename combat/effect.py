class Effect:
    def __init__(self, name, power, timer, affected_stat):
        self.name = name
        self.power = power
        self.timer = timer
        self.affected_stat = affected_stat

    def timer_handler(self):
        print("TICKING TIMER")
        self.timer -= 1
        if self.timer == 0:
            return True
        else:
            return False

    def apply_effect(self, stat):
        return stat * (self.power / 100)



