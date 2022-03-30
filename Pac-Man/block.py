import pyray as pr
class Block:
    def __init__(self,pos) -> None:
        print(pos)
        self.x = pos['x']
        self.y = pos['y']
        self.w = pos['w']
        self.h = pos['h']
        # a = {}
        # a['x'] = 10
        # self = a
        # for key, val in pos.items():
        #     print(key, val)
        #     a[key] = val
        # self = a

    def display(self):
        pr.draw_rectangle(self.x, self.y, self.w, self.h,pr.BLUE)      