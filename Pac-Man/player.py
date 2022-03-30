from constants import BLOCKSIZE as BSIZE
import constants as const
import pyray as pr
from keyboard_service import Keyboard


class Player:
    def __init__(self, pos) -> None:
        print(pos)
        self.x = int(pos['x']+(BSIZE-pos['w'])/2)
        self.y = int(pos['y']+(BSIZE-pos['h'])/2)
        self.w = pos['w']
        self.h = pos['h']
        self.keyboard = Keyboard()
        self.speed = const.PLAYERSPEED
        self.vel = pr.Vector2(self.speed, 0)
        
        self.rect = pr.Rectangle(self.x, self.y, self.w, self.h)

    def display(self):
        self.rect = pr.Rectangle(self.x, self.y ,self.w ,self.h)
        # pr.draw_rectangle(0, 0, self.w, self.h, pr.RED)
        pr.draw_rectangle_rec(self.rect, pr.RED)


    def moveX(self):
        if(self.keyboard.is_pressed('a')):
            self.vel = pr.Vector2(-self.speed, 0)
        if(self.keyboard.is_pressed('d')):
            self.vel = pr.Vector2(self.speed, 0)

    def moveY(self):
        if(self.keyboard.is_pressed('w')):
            self.vel = pr.Vector2(0, -self.speed)
        if(self.keyboard.is_pressed('s')):
            self.vel = pr.Vector2(0, self.speed)

    def move(self):
        self.prev = pr.Vector2(self.x, self.y)

        self.moveX()
        self.x += int(self.vel.x)
        self.xCollide()

        self.moveY()
        self.y += int(self.vel.y)
        self.yCollide()

    def collide(self, a, b):
        return (
            a.x - b.x < b.w and
            b.x - a.x < a.w and
            a.y - b.y < b.h and
            b.y - a.y < a.h
        )

    def xCollide(self):
        for i in range(len(const.blocks)):
            if(self.collide(self, const.blocks[i])):
                b = const.blocks[i]

                self.x = int(b.x - self.w if self.prev.x < b.x else b.x + b.w)
                self.vel = pr.Vector2(0,0)

    def yCollide(self):
        for i in range(len(const.blocks)):
            if(self.collide(self, const.blocks[i])):
                b = const.blocks[i]
                self.y = int(b.y - self.h if self.prev.y < b.y else b.y + b.h)
                self.vel = pr.Vector2(0,0)
