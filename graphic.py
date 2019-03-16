"""
Copy right Thanh Thuan
file GUI
"""
import pyglet
from pyglet.window import mouse
from time import sleep


def take_data():
    """
    take data to handle from data file
    @param : none
    @return list_redo : The list contain moves of number on display
    @return list_draw : The list contain objects that contain numbers to draw
    @return name_algo : name of algorithm being use
    """
    f = open('data', 'r')  # open file data
    list_data = f.read().split('\n')[:-1]
    name_algo = list_data[0]  # take name of algorithm

    # Create a list contain text object to draw
    list_draw = []
    for index, number in enumerate(list_data[1].split(' ')):
        list_draw.append(pyglet.text.Label(number, font_size=20,
                                           x=80*(index+1), y=360))

    # Create a list contain
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


def swap(object_a, object_b):
    """
    swap position and content of object A and object B
    @param : object A and B (pyglet.text.Label)
    @return : None
    """
    object_a.x, object_b.x = object_b.x, object_a.x
    object_a.text, object_b.text = object_b.text, object_a.text


class Arrow:
    """
    declare arrow on display
    Posx : position x of arrow_pivot
    Posy : default is 400
    """
    def __init__(self, posx, image):
        self.Sprite = pyglet.sprite.Sprite(image)
        self.posx = posx
        self.Sprite.x = 80*(self.posx+1) - 22
        self.Sprite.y = 400

    def update(self):
        self.Sprite.x = 80*(self.posx+1) - 22


class Graphic(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        """
        declare and set all attributes of window
        inherit attributes from pyglet.window.Window
        get data from file data and convert it become list to handle
        """
        super().__init__(*args, **kwargs)
        self.frame_rate = 1/60.0  # set time run

        # take data to handle
        self.list_redo, self.list_draw, name = take_data()

        # declare pivot if the program using quick sort
        if name == 'quick':
            self.list_pivot = []
            self.arrow_pivot = pyglet.image.load('pivot.png')
            for x in self.list_redo:
                self.list_pivot.append(x.pop())
            self.list_pivot.insert(0, self.list_pivot[0])

        # determine index current
        self.index_current = 0
        # insert index current at the top of the list
        self.list_redo.insert(0, self.index_current)
        # index of list redo
        self.index = 0
        # True if the number being change (when click left mouse)
        self.wait = False

        """
        declare text, backgrond and arrow image
        """
        self.sorted = pyglet.text.Label('List have been sorted',
                                        font_size=40, x=300, y=200)
        self.step = pyglet.text.Label('Step :' + '    /' +
                                      str(len(self.list_redo) - 1),
                                      font_size=30, x=1000, y=600)
        self.step_run = pyglet.text.Label('1', font_size=30, x=1120, y=600)
        self.algo = pyglet.text.Label(name, font_size=30, x=580, y=600)

        self.arrow = pyglet.image.load('arrow.png')
        self.list_arrow = [Arrow(self.list_redo[1][0], self.arrow),
                           Arrow(self.list_redo[1][-1], self.arrow)]

        back_tmp = pyglet.image.load('bg.jpg')
        self.back_ground = pyglet.sprite.Sprite(img=back_tmp)

    def on_draw(self):
        """
        draw all object in Window include : text, number, arrow, ...
        """
        self.clear()
        # draw backgrond and text (number of steps, name of algorithm)
        self.back_ground.draw()
        self.algo.draw()
        self.step.draw()
        self.step_run.draw()

        # draw list need sort
        for element in self.list_draw:
            element.draw()

        # draw arrow and the move of it (when click left mouse)
        if self.wait:
            for x in self.list_arrow:
                x.Sprite.draw()

        # draw pivot have been chosen (if the algorithm is quick sort)
        if self.algo.text == 'quick':
            Arrow(self.list_pivot[self.index], self.arrow_pivot).Sprite.draw()

        # only draw when finished
        if self.index == self.index_current == len(self.list_redo) - 1:
            self.sorted.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Working with mouse event (mouse LEFT)
        """
        if button == mouse.LEFT and self.index < len(self.list_redo) - 1\
           and not self.wait:
            self.index += 1

    def move_pos_arrow(self, step):
        """
        change position of arrow
        the program will stop 0.5s after change
        @param : step Will determine arrow will go forward or go backward
        @return none
        """
        self.list_arrow[0].posx += step
        sleep(0.5)

    def move_number(self, start, end, index, step1):
        """
        move number on display
        @param : start The index start of list which contain all number
                 need move go forward
        @param : end The index end of list which contain all number
                 need move go forward
        @param : index The index of number need go backward
        @param : step1 The speed of the numbers need go forward
        @return None
        """
        # move all element in list[start:end] move by step1
        for pos in self.list_redo[self.index][start:end]:
            self.list_draw[pos].x += step1

        # determine speed of the number need go backward
        step2 = step1 * -len(self.list_redo[self.index][start:end])
        self.list_draw[index].x += step2

    def update_pos_arrow_number(self, index_left, index_right):
        """
        update position of numbers and arrows when it was moved
        @param : index_left Index of point left
        @param : index_right Index of point right
        @return None
        """
        self.wait = False
        self.index_current = self.index

        """
        determine list update base on index_left and index_right
        only take index left and index right if the algorithm is quick sort
        or take all element from index left to index right (bubble, merge, ...)
        """
        if self.algo.text == 'quick':
            list_update = [index_left, index_right]
        else:
            list_update = list(range(index_left, index_right))

        # swap content and position
        for z in list_update:
            swap(self.list_draw[index_right], self.list_draw[z])

        # update position of arrow base on list redo and current index + 1
        try:
            self.list_arrow[0].posx = self.list_redo[self.index + 1][-1]
            self.list_arrow[1].posx = self.list_redo[self.index + 1][-1]
        except IndexError:
            pass

    def handle_arrow_number(self, dt, left, move, move1):
        """
        handle all arrow and number
        move and update position of arrow, list
        @param : left The index where the arrow left need go
        @param : move Determine position arrow left
                      will go forward or go backward
        @param : move1 Determine the move of elemnet right
        @return None
        """
        if self.index_current != self.index:
            self.wait = True
            index_right = self.list_redo[self.index][-1]
            index_left = self.list_redo[self.index][left]

            if self.list_arrow[0].posx != index_left:
                self.move_pos_arrow(move)

            elif self.list_draw[index_right].x != 80*(index_left+1):
                self.move_number(left, -1, index_right, move1)

            else:
                self.update_pos_arrow_number(index_left, index_right)

    def update(self, dt):
        """
        update main
        it will update coordinate of number in list and arrow
        @param : dt Run time
        @return : None
        """
        self.step_run.text = str(self.index)
        if self.algo.text == 'quick':
            self.handle_arrow_number(dt, -2, 1, -5)
        else:
            self.handle_arrow_number(dt, 0, -1, 1)
        self.list_arrow[0].update()
        self.list_arrow[1].update()


def main():
    """
    run app
    """
    game = Graphic(1280, 720, 'Simulator Sort')
    pyglet.clock.schedule_interval(game.update, game.frame_rate)
    pyglet.app.run()


if __name__ == '__main__':
    main()
