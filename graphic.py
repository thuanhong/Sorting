import pyglet
from time import sleep
from pyglet.window import mouse, key


class num:
    def __init__(self, value, posx, posy, colour = (255, 255, 255, 255), move = None):
        self.num = pyglet.text.Label(str(value), font_size = 20,x = posx,y = posy, color = colour)
        self.posx = posx
        self.posy = posy

    def draw(self):
        self.num.draw()

    def update(self, dt):
        pass

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
        self.temp = [3,6,3,7,43,8,3,8,4,8,4]
        self.image = pyglet.image.load('image.png')
        # self.list = []
        # for x, y in enumerate(self.temp):
        #     self.list.append(num(y, 100*(x+1), 360))

    def on_draw(self):
        self.clear()
        for x, y in enumerate(self.temp):
            num(y, 100*(x+1), 360).draw()
        # square(100*(y+1), 360, self.image).draw()
        # square(100*(y+1+1), 360, self.image).draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            n = len(self.temp)
            for y in range(n - 1):
                if self.temp[y+1] < self.temp[y]:
                    self.temp[y+1], self.temp[y] = self.temp[y], self.temp[y+1]

                    # self.list[y+1], self.list[y] = self.list[y], self.list[y+1]
                    # print('sfgdfg')
                    # for x in self.list:
                    #     print(x.num.text, end =' ')

    def update(self, dt):
        pass




if __name__ == '__main__':
    game = gameWindow(1280, 720)
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()
