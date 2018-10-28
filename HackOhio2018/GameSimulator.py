class Pitcher:

    def __init__(self,name, strike, ball, bip, hr):
        self.name = name
        self.strike = 0.0
        self.ball = 0.0
        self.bip = 0.0
        self.hr = 0.0

    def Name(self):
        return self.name

    def Strike(self):
        return self.strike

    def Ball(self):
        return self.ball

    def bip(self):
        return self.bip

    def hr(self):
        return self.hr

class Batter:

    def __init__(self, name, bip, hr):
        self.name = name
        self.bip = 0.0
        self.hr = 0.0

    def Name(self):
        return self.name

    def Bip(self):
        return self.bip

    def Hr(self):
        return self.hr


class Pitch(Pitcher,Hitter):

    def __init__(self, outcome)
