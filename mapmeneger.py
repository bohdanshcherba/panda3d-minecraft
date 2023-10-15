class MapMeneger():
    def __init__(self):
        self.startNew()
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0, 1),
        ]

    def getColor(self, z):
        if z < 4:
            return self.colors[z]
        else: 
            return self.colors[4]
        

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position, texture):
        model = loader.loadModel("models/blocks/block.egg")
        texture = loader.loadTexture(f"models/blocks/{texture}.png")
        model.setTexture(texture)
        model.setPos(position)
        color = self.getColor(position[2])
        model.setColor(color)
        model.reparentTo(self.land)

    def loadLand(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
            
                line = line.split(" ")
                x = 0
                for z in line:
                    for z0 in range(int(z)+1):
                        self.addBlock((int(x), int(y),int(z0)), 'block' )
                    x+=1
                y+=1