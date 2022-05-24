from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False


    def use_tongue_to_smell(self):
        print("Smelling through my tongue")


Sidney = Snake()
Sidney.breathe()


