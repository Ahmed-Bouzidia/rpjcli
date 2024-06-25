class Personnage:
    HEART_LOOSED_POINTS = 20

    def __init__(self):
        self.points = 100
        self.isAlive = True
        self.position = (1,1)

    def get_points(self):
        return self.points

    def is_alive(self):
        return self.isAlive

    def attack(self, victime):
        victime.points -= 1

    def hurt(self, victime):
        victime.points -= self.HEART_LOOSED_POINTS
        if victime.points == 0:
            victime.isAlive = False

    def run(self): #run form a position to another one
        self.position = (1,3)

    def get(self):
        return 1