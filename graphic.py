import pyglet
from time import sleep
from pyglet.window import mouse, key
from sorting_deck import *


class num:
    def __init__(self, value, posx, posy, colour = (255, 255, 0, 255), move = None):
        self.num = pyglet.text.Label(str(value), font_size = 20,x = posx,y = posy, color = colour)
        self.posx = posx
        self.posy = posy

    def draw(self):
        self.num.draw()

class square:
    def __init__(self, x, y, img = None):
        self.x = x
        self.y = y
        if img != None:
            self.sprite = pyglet.sprite.Sprite(img)
            self.sprite.x = self.x
            self.sprite.y = self.y

    def draw(self):
        self.sprite.draw()


class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0

        self.list = []

        f = open('data', 'r')  # take data to handle from data file
        for x in f.read().split('\n')[:-1]:
            temp = []
            for y in x:
                try:
                    temp.append(int(y))
                except ValueError:
                    pass
            self.list.append(temp)
        f.close()

        self.sorted = pyglet.text.Label('List have been sorted', font_size = 40,x = 700,y = 200)
        # for x, y in enumerate(self.temp):
        #     self.list.append(num(y, 100*(x+1), 360))

        self.image = pyglet.image.load('image.png')
        back_tmp = pyglet.image.load_animation('bg.gif')
        self.back_ground = pyglet.sprite.Sprite(img=back_tmp)
        self.back_ground.update(scale_x=self.width/self.back_ground.width, scale_y=self.height/self.back_ground.height)
        self.y = 1
        self.count = 0

    def on_draw(self):
        self.clear()
        self.back_ground.draw()
        # square(100*(self.y+1), 354, self.image).draw()
        # square(100*(self.y+1+1), 354, self.image).draw()
        for x, y in enumerate(self.list[self.count]):
            num(y, 100*(x+1), 360).draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            pass


    def update(self, dt):



    def update(self):
        self.posx = move

if __name__ == '__main__':
    game = gameWindow(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()
