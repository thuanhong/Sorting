import pyglet
from pyglet.window import mouse, key
from sorting_deck import *
import math


class num:
    def __init__(self, value, posx, posy):
        self.num = pyglet.text.Label(value, font_size = 20,x = posx,y = posy)

    def draw(self):
        self.num.draw()


def take_data():

    f = open('data', 'r')  # take data to handle from data file
    list_data = f.read().split('\n')[:-1]

    list_draw = []
    for index, number in enumerate(list_data[0].split(' ')):
        list_draw.append(num(number, 100*(index+1), 360))

    list_redo = []
    # list_undo = []
    for line in list_data[1:]:
        temp = []
        for y in line.split(' '):
            temp.append(int(y))
        list_redo.append(temp)
        # list_undo.append([int(line[2]), int(line[0])])
    f.close()

    return list_redo, list_draw

class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0

        self.list_redo, self.list_draw = take_data()
        self.cor_cur = self.list_redo[0][::-1]
        self.list_redo.insert(0, self.cor_cur)
        self.len = len(self.list_redo) - 1
        print(self.cor_cur)


        self.count = 0
        self.wait = False

        self.sorted = pyglet.text.Label('List have been sorted',
                                        font_size = 40,x = 300,y = 200)
        self.step = pyglet.text.Label('Step :' + '   /' + str(len(self.list_draw)+1),
                                        font_size = 30,x = 1000,y = 600)
        self.current = pyglet.text.Label('1', font_size = 30,x = 1120,y = 600)

        self.image = pyglet.image.load('image.png')
        back_tmp = pyglet.image.load('bg.jpg')
        self.back_ground = pyglet.sprite.Sprite(img=back_tmp)


    def on_draw(self):
        self.clear()
        self.back_ground.draw()

        for x in self.list_draw:
            x.draw()
        self.step.draw()
        self.current.draw()
        if self.count == len(self.list_redo) - 1:
            self.sorted.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.count < self.len and not self.wait:
            self.count += 1
    #     # elif button == mouse.RIGHT and self.count > 0 and not self.wait:
    #     #     self.count -= 1
    #
    # def update_bubble(self, dt):
    #     if self.cor_cur != self.list_redo[self.count]:
    #         self.wait = True
    #         index = self.list_redo[self.count][0]
    #         temp = self.list_redo[self.count][1]
    #         if self.list_draw[index].num.x != 100*(temp+1):
    #             self.list_draw[index].num.x += 2
    #             self.list_draw[temp].num.x -= 2
    #         else:
    #             self.cor_cur = self.list_redo[self.count]
    #             self.wait = False
    #             self.list_draw[index].num.x, self.list_draw[temp].num.x = self.list_draw[temp].num.x, self.list_draw[index].num.x
    #             self.list_draw[index].num.text, self.list_draw[temp].num.text = self.list_draw[temp].num.text, self.list_draw[index].num.text

    def update_insert(self, dt):
        if self.cor_cur != self.list_redo[self.count]:
            self.wait = True
            for x in self.list_redo[self.count][:-1]:
                if self.list_draw[x].num.x != 100*(x+1+1):
                    self.list_draw[x].num.x += 2

    def update(self, dt):
        self.current.text = str(self.count)
        # self.update_bubble(dt)
        self.update_insert(dt)

if __name__ == '__main__':
    game = gameWindow(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()
