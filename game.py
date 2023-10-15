from direct.showbase.ShowBase import ShowBase
from mapmeneger import MapMeneger

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapMeneger()
        self.land.loadLand("land.txt")


game = Game()
game.run()