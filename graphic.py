import pyglet
from pyglet.window import mouse


def take_data():

    f = open('data', 'r')  # take data to handle from data file
    list_data = f.read().split('\n')[:-1]
    list_draw = []
    for index, number in enumerate(list_data[0].split(' ')):
        list_draw.append(pyglet.text.Label(number, font_size = 20, x=100*(index+1), y=360))

    list_redo = []
    for line in list_data[1:]:
        temp = []
        for y in line.rstrip().split(' '):
            temp.append(int(y))
        list_redo.append(sorted(list(set(temp))))
    f.close()
    return list_redo, list_draw

class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0

        self.list_redo, self.list_draw = take_data()
        self.cor_cur = self.list_redo[0][::-1]
        self.list_redo.insert(0, self.cor_cur)

        self.count = 0
        self.wait = False

        self.sorted = pyglet.text.Label('List have been sorted',
                                        font_size = 40,x = 300,y = 200)
        self.step = pyglet.text.Label('Step :' + '   /' + str(len(self.list_redo)+1),
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
        if button == mouse.LEFT and self.count < len(self.list_redo) - 1 and not self.wait:
            self.count += 1
        # elif button == mouse.RIGHT and self.count > 0 and not self.wait:
        #     self.count -= 1

    def update_insert_bubble(self, dt):
        if self.cor_cur != self.list_redo[self.count]:
            self.wait = True
            index = self.list_redo[self.count][-1]
            temp = self.list_redo[self.count][0]
            if self.list_draw[index].x != 100*(temp+1):
                for x in self.list_redo[self.count][:-1]:
                    self.list_draw[x].x += 1
                self.list_draw[index].x -= len(self.list_redo[self.count][:-1])

            else:
                self.cor_cur = self.list_redo[self.count]
                for z in range(temp, index):
                    self.list_draw[index].x, self.list_draw[z].x = self.list_draw[z].x, self.list_draw[index].x
                    self.list_draw[index].text, self.list_draw[z].text = self.list_draw[z].text, self.list_draw[index].text
                self.wait = False


    def update(self, dt):
        self.current.text = str(self.count)
        # self.update_bubble(dt)
        self.update_insert_bubble(dt)


def main():
    game = gameWindow(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()

if __name__ == '__main__':
    main()
