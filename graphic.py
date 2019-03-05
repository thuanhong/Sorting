import pyglet

class gameWindow(pyglet.window.Window):
    def __init__(*args, **kwargs):
        super().__init__(self, *args, **kwargs):
        self.frame_rate = 1/60.0


if __name__ == '__main__':
    game = window(1280, 720)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
