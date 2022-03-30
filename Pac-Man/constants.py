LEVEL = 0
BOARDS = [
    [
        ' bbb bbbb',
        'b       b',
        'b bb bb b',
        'b b   b b',
        'b   p   b',
        'b b   b b',
        'b bb bb b',
        'b       b',
        'bbbbbbbbb',
    ],
]

CANVASSIZE = 450
BLOCKSIZE = int((CANVASSIZE/len(BOARDS[LEVEL]))*0.9)
PLAYERSIZE =20 # int(BLOCKSIZE*0.8)
FPS = 60
PLAYERSPEED = 3


blocks = []
coins = []
ghosts = []
player = None