from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


    def digest_large_prey(self):
        print("I've eaten something large")

    def constrict(self):
        print("Squeeze")

    def climb(self):
        print("climbing")


    def shed_skin(self):
        print("I am shedding")

peter = Python()
peter.breathe()