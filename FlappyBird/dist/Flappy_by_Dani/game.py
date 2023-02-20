import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
import pkg_resources.py2_warn
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', '0')

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


Builder.load_file("features.kv")


def randgen():
    return randint(0, 300)

class Bird(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, *args, **kwargs):
        super(Bird, self).__init__()
        self.y = 250

    def move(self):
        self.y = Vector(*self.velocity)[1] + self.y

class Wall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)


    def move(self):
        self.x = Vector(*self.velocity)[0] + self.x

class Hole(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)


    def move(self):
        self.x = Vector(*self.velocity)[0] + self.x

class mainScreen(Widget):
    Window.clearcolor = (0.3, 0.6, 1, 1)
    spd = 4
    g = -10
    delta_t = 0.01
    bird = ObjectProperty(None)
    counter1 = 0
    score = StringProperty(str(counter1))
    wspd = -3
    block = []
    last_state = False
    this_state = False
    counter2 = 0
    attempts = StringProperty(str(counter2))
    counter3 = 0
    best = StringProperty(str(counter3))
    gover = ''
    gameoverlabel = StringProperty(gover)
    pause = False

    def resuming(self):
        self.pause = False

    w1 = ObjectProperty(None)
    w2 = ObjectProperty(None)
    w3 = ObjectProperty(None)
    h1 = ObjectProperty(None)
    h2 = ObjectProperty(None)
    h3 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(mainScreen, self).__init__()
        self._keyboard = Window.request_keyboard(self.on_keyboard_down, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        self.score = str(0)
        self.w1.x = randint(800, 950)
        self.w2.x = randint(1200, 1350)
        self.w3.x = randint(1600, 1750)
        self.h1.x = self.w1.x
        self.h2.x = self.w2.x
        self.h3.x = self.w3.x

        self.h1.y = randint(20, 300)
        self.h2.y = randint(20, 300)
        self.h3.y = randint(20, 300)

        self.block.append(875)
        self.block.append(875)
        self.block.append(875)

    def restart(self):
        self.gover = ''
        self.gameoverlabel = self.gover
        self.last_state = False
        self.bird.y = 250
        self.spd = 0
        self.counter1 = 0
        self.counter2 += 1
        self.score = str(self.counter1)
        self.attempts = str(self.counter2)
        self.w1.x = randint(800, 950)
        self.w2.x = randint(1200, 1350)
        self.w3.x = randint(1600, 1750)
        self.h1.x = self.w1.x
        self.h2.x = self.w2.x
        self.h3.x = self.w3.x
        self.wspd = -3
        self.h1.y = randint(20, 300)
        self.h2.y = randint(20, 300)
        self.h3.y = randint(20, 300)

        self.block[0] = 875
        self.block[1] = 875
        self.block[2] = 875

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'spacebar':
            self.spd += 8
        return True


    def serve_bird(self):
        #self.bird.center = self.center
        self.bird.velocity = Vector(0, self.spd)

        self.w1.velocity = Vector(self.wspd, 0)
        self.w2.velocity = Vector(self.wspd, 0)
        self.w3.velocity = Vector(self.wspd, 0)
        self.h1.velocity = Vector(self.wspd, 0)
        self.h2.velocity = Vector(self.wspd, 0)
        self.h3.velocity = Vector(self.wspd, 0)


    def update(self, dt):
        if (self.pause is False):
            if (self.w1.collide_widget(self.bird) is True and self.h1.collide_widget(self.bird) is False):
                self.gover = 'GAME OVER'
                self.gameoverlabel = self.gover
                self.pause = True

            if (self.w2.collide_widget(self.bird) is True and self.h2.collide_widget(self.bird) is False):
                self.gover = 'GAME OVER'
                self.gameoverlabel = self.gover
                self.pause = True

            if (self.w3.collide_widget(self.bird) is True and self.h3.collide_widget(self.bird) is False):
                self.gover = 'GAME OVER'
                self.gameoverlabel = self.gover
                self.pause = True

            if(self.h1.collide_widget(self.bird) is True or self.h2.collide_widget(self.bird) is True or self.h3.collide_widget(self.bird) is True):
                self.this_state = True
            else:
                self.this_state = False

            if(self.last_state is True and self.this_state is False):
                self.counter1+=1
                self.score = str(self.counter1)
                self.wspd = self.wspd - 0.1
                if(self.counter3 < self.counter1):
                    self.counter3 = self.counter1
                    self.best = str(self.counter3)


            self.last_state = self.this_state
            self.bird.move()
            self.w1.move()
            self.w2.move()
            self.w3.move()
            self.h1.move()
            self.h2.move()
            self.h3.move()

            self.spd = self.spd + (self.g*self.delta_t)
            self.bird.velocity = Vector(0, self.spd)
            self.w1.velocity = Vector(self.wspd, 0)
            self.w2.velocity = Vector(self.wspd, 0)
            self.w3.velocity = Vector(self.wspd, 0)
            self.h1.velocity = Vector(self.wspd, 0)
            self.h2.velocity = Vector(self.wspd, 0)
            self.h3.velocity = Vector(self.wspd, 0)

            if(self.w1.x < self.block[0]-1100):
                self.block[0] = randint(800, 950)
                self.w1.x = self.block[0]
                self.h1.x = self.block[0]
                self.h1.y = randint(20, 300)
            if (self.w2.x < self.block[1]-1100):
                self.block[1] = randint(800, 950)
                self.w2.x = self.block[1]
                self.h2.x = self.block[1]
                self.h2.y = randint(20, 300)
            if (self.w3.x < self.block[2]-1100):
                self.block[2] = randint(800, 950)
                self.w3.x = self.block[2]
                self.h3.x = self.block[2]
                self.h3.y = randint(20, 300)


            if (self.bird.y < 0) or (self.bird.top > self.height+40):
                self.gover = 'GAME OVER'
                self.gameoverlabel = self.gover
                self.pause = True

class GameApp(App):

    def build(self):
        game = mainScreen()
        game.serve_bird()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


GameApp().run()