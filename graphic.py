import pyglet
from pyglet.window import mouse
from time import sleep


def take_data(width):

    f = open('data', 'r')  # take data to handle from data file
    list_data = f.read().split('\n')[:-1]
    list_draw = []
    name_algo = list_data[0]
    for index, number in enumerate(list_data[1].split(' ')):
        list_draw.append(pyglet.text.Label(number, font_size = 20, x=100*(index+1), y=360))

    list_redo = []
    for line in list_data[2:]:
        temp = []
        for y in line.rstrip().split(' '):
            temp.append(int(y))
        if name_algo != 'quick':
            list_redo.append(sorted(temp))
        else:
            list_redo.append(temp)
    f.close()
    return list_redo, list_draw, name_algo

class arrow:
    def __init__(self, posx, image):
        self.Sprite = pyglet.sprite.Sprite(image)
        self.posx = posx
        self.Sprite.x = 100*(self.posx+1) - 23
        self.Sprite.y = 400

    def update(self):
        self.Sprite.x = 100*(self.posx+1) - 23


class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0

        self.list_redo, self.list_draw, name = take_data(self.width)
        if name == 'quick':
            self.list_pivot = []
            self.arrow_pivot = pyglet.image.load('pivot.png')
            for x in self.list_redo:
                self.list_pivot.append(x.pop())
            self.list_pivot.insert(0, 9)

        self.cor_cur = 0
        self.list_redo.insert(0, self.cor_cur)

        self.count = 0
        self.wait = False

        self.sorted = pyglet.text.Label('List have been sorted',
                                        font_size = 40,x = 300,y = 200)
        self.step = pyglet.text.Label('Step :' + '    /' + str(len(self.list_redo) - 1),
                                        font_size = 30,x = 1000,y = 600)
        self.current = pyglet.text.Label('1', font_size = 30,x = 1120,y = 600)
        self.algo = pyglet.text.Label(name, font_size = 30,x = 580,y = 600)

        self.arrow = pyglet.image.load('arrow.png')
        self.list_arrow = [arrow(self.list_redo[1][0], self.arrow),
                          arrow(self.list_redo[1][-1], self.arrow)]
        back_tmp = pyglet.image.load('bg.jpg')
        self.back_ground = pyglet.sprite.Sprite(img=back_tmp)

    def on_draw(self):
        self.clear()
        self.back_ground.draw()
        self.algo.draw()
        for x in self.list_draw:
            x.draw()
        if self.wait:
            for x in self.list_arrow:
                x.Sprite.draw()
        if self.algo.text == 'quick':
            arrow(self.list_pivot[self.count], self.arrow_pivot).Sprite.draw()


        self.step.draw()
        self.current.draw()
        if self.count == self.cor_cur == len(self.list_redo) - 1:
            self.sorted.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.count < len(self.list_redo) - 1 and not self.wait:
            self.count += 1

    def move_pos_arrow(self, step):
        self.list_arrow[0].posx += step
        self.list_arrow[0].update()
        sleep(0.5)

    def move_number(self, start, end, index, step1, step2):
        for pos in self.list_redo[self.count][start:end]:
            self.list_draw[pos].x += step1
        self.list_draw[index].x += step2

    def update_pos_arrow_number(self, index, list):
        self.cor_cur = self.count
        for z in list:
            self.list_draw[index].x, self.list_draw[z].x = self.list_draw[z].x, self.list_draw[index].x
            self.list_draw[index].text, self.list_draw[z].text = self.list_draw[z].text, self.list_draw[index].text
        try:
            self.list_arrow[0].posx = self.list_redo[self.count + 1][-1]
            self.list_arrow[1].posx = self.list_redo[self.count + 1][-1]
            self.list_arrow[0].update()
            self.list_arrow[1].update()
        except:
            pass
        self.wait = False

    def update_insert_bubble(self, dt):
        if self.cor_cur != self.count:
            self.wait = True
            index = self.list_redo[self.count][-1]
            temp = self.list_redo[self.count][0]

            if self.list_arrow[0].posx != temp:
                self.move_pos_arrow(-1)

            elif self.list_draw[index].x != 100*(temp+1):
                step2 = -len(self.list_redo[self.count][:-1])
                self.move_number(0, -1, index, 1, step2)

            else:
                self.update_pos_arrow_number(index, list(range(temp, index)))

    def update_quick(self, dt):
        if self.cor_cur != self.count:
            self.wait = True
            index = self.list_redo[self.count][-1]
            temp = self.list_redo[self.count][-2]

            if self.list_arrow[0].posx != temp:
                self.move_pos_arrow(1)

            elif self.list_draw[index].x != 100*(temp+1):
                self.move_number(-2, -1, index, -5, 5)

            else:
                self.update_pos_arrow_number(index, [temp, index])

    def update(self, dt):
        self.current.text = str(self.count)
        if self.algo.text == 'quick':
            self.update_quick(dt)
        else:
            self.update_insert_bubble(dt)


def main():
    game = gameWindow(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()

if __name__ == '__main__':
    main()
