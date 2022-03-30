import pyray as pr
import constants as const
from player import Player
from block import Block

class Game:
    def __init__(self) -> None:
        self.created = False
        self.camera = pr.Camera2D()
        self.camera.rotation = 0.0
        self.camera.zoom = 1.0
        self.camera.offset = pr.Vector2(const.CANVASSIZE/2.0, const.CANVASSIZE/2.0)
        
    def createLevel(self):
        for i in range(len(const.BOARDS[const.LEVEL])):
            for j in range(len(const.BOARDS[const.LEVEL][i])):
                id = const.BOARDS[const.LEVEL][i][j]
                if(id == 'p'):
                    const.player = (Player({
                        'x': j*const.BLOCKSIZE,
                        'y': i*const.BLOCKSIZE,
                        'w': const.PLAYERSIZE,
                        'h': const.PLAYERSIZE,
                    }))
                    # self.camera.target = pr.Vector2(const.player.x + 20.0, const.player.y + 20.0)
                    self.camera.offset = pr.Vector2(const.CANVASSIZE/2.0, const.CANVASSIZE/2.0)
                elif(id == 'b'):
                    const.blocks.append(Block({
                        'x': j*const.BLOCKSIZE,
                        'y': i*const.BLOCKSIZE,
                        'w': const.BLOCKSIZE,
                        'h': const.BLOCKSIZE,
                    }))
        self.created = True
    def display(self):
        for i in range(len(const.blocks)):
            const.blocks[i].display()
        const.player.display()

    def update(self):
        const.player.move()
        self.updateCamera()
    
    def updateCamera(self):
        self.camera.target = pr.Vector2(const.player.x + const.player.w/2, const.player.y + const.player.h/2)
    
    def run(self):
        if not self.created:
            self.createLevel()
            print('Created level')
        else: 
            pr.begin_mode_2d(self.camera)
            self.update()
            self.display()
            pr.end_mode_2d()