import pyglet
from time import sleep
from pyglet.window import mouse, key
from sorting_deck import *


class num:
    def __init__(self, value, posx, posy):
        self.num = pyglet.text.Label(str(value), font_size = 20,x = posx,y = posy)

    def draw(self):
        self.num.draw()


# class square:
#     def __init__(self, x, y, img = None):
#         self.x = x
#         self.y = y
#         if img != None:
#             self.sprite = pyglet.sprite.Sprite(img)
#             self.sprite.x = self.x
#             self.sprite.y = self.y
#
#     def draw(self):
#         self.sprite.draw()


def take_data():
    list_num = []
    f = open('data', 'r')  # take data to handle from data file
    for line in f.read().split('\n')[:-1]:
        temp = []
        for y in line.split(' '):
            temp.append(int(y))
        list_num.append(temp)
    f.close()
    list_draw = []
    for index, number in enumerate(list_num[0]):
        list_draw.append(num(number, 100*(index+1), 360))
    return list_num, list_draw

class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0

        self.list_num, self.list_draw = take_data()
        self.count = 0

        self.sorted = pyglet.text.Label('List have been sorted',
                                        font_size = 40,x = 300,y = 200)
        self.step = pyglet.text.Label('Step :' + '  /' + str(len(self.list_draw)),
                                        font_size = 30,x = 1000,y = 600)
        self.current = pyglet.text.Label(str(self.count+1),
                                        font_size = 30,x = 1120,y = 600)

        self.image = pyglet.image.load('image.png')
        back_tmp = pyglet.image.load('bg.jpg')
        self.back_ground = pyglet.sprite.Sprite(img=back_tmp)


    def on_draw(self):
        self.clear()
        self.back_ground.draw()
        # square(100*(self.y+1), 354, self.image).draw()
        # square(100*(self.y+1+1), 354, self.image).draw()
        for x in self.list_draw:
            x.draw()
        self.step.draw()
        self.current.draw()
        if self.count == len(self.list_draw) - 1:
            self.sorted.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.count < len(self.list_draw):
            self.count += 1
            self.current.text = str(self.count)
        elif button == mouse.RIGHT and self.count > 0:
            self.count -= 1
            self.current.text = str(self.count)

    def update_bubble(self, dt):
        for index, number in enumerate(self.list_num[self.count]):
            if str(number) != self.list_draw[index].num.text:
                temp = index+1
                # while self.list_draw[index].num.x != 100*(temp+1):
                #     self.list_draw[index].num.x -= -2
                #     self.list_draw[temp].num.x += -2
                #     break
                # else:
                #     self.list_draw[index].num.x, self.list_draw[temp].num.x = self.list_draw[temp].num.x, self.list_draw[index].num.x
                #     self.list_draw[index].num.text, self.list_draw[temp].num.text = self.list_draw[temp].num.text, self.list_draw[index].num.text
                # break
                

    def update(self, dt):
        self.update_bubble(dt)

if __name__ == '__main__':
    game = gameWindow(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()
