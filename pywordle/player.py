class Player:
    def __init__(self):
        self.ATTEMPTS = 0

    def lost_attempt(self):
        self.ATTEMPTS += 1