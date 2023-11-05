from direct.showbase.ShowBase import ShowBase
from mapmeneger import MapMeneger
from hero import Hero
from direct.gui.OnscreenText import OnscreenText
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapMeneger()
        self.land.loadLand("land.txt")
        self.hero = Hero((0,0,1), self.land)
        #textObject = OnscreenText(text='my text string', pos=(1, 0.7), scale=0.07)


game = Game()
game.run()