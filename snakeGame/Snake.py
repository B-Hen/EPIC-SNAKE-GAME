import pyglet


#class to create the snake player
class Player:
    def __init__(self, pos_x, pos_y, width, height):
        self.x = pos_x
        self.y = pos_y
        self.vel_x = 130
        self.vel_y = 0
        self.width = width
        self.height = height

        image = pyglet.image.load("images/greenBlock.jpg")
        image.width = self.width
        image.height = self.height
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y)

    def draw(self):
        self.sprite.draw()

    def update(self):
        self.sprite.x += self.vel_x * (1/60)
        self.sprite.y += self.vel_y * (1/60)






