import pyglet
import random


#class to create the snake player
class Player(object):
    def __init__(self, pos_x, pos_y, size, velocity):
        self.x = pos_x
        self.y = pos_y
        #starts snake in random direction
        randstart = random.randint(1, 4)
        if randstart == 1:
            self.vel_x = velocity
            self.vel_y = 0
        elif randstart == 2:
            self.vel_x = -velocity
            self.vel_y = 0
        elif randstart == 3:
            self.vel_y = velocity
            self.vel_x = 0
        elif randstart == 4:
            self.vel_y = -velocity
            self.vel_x = 0
        self.width = size
        self.height = size

        image = pyglet.image.load("images/greenBlock.jpg")
        image.width = size
        image.height = size
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y)

    def draw(self):
        self.sprite.draw()

    def update(self):
        self.sprite.x += self.vel_x * (1/100)
        self.sprite.y += self.vel_y * (1/100)






