import pyglet
from pyglet.gl import *
import math
import tkinter as tk
from Snake import Player
from pyglet.window import key
import random


#create the game window
class GameWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(100, 200)
        self.frame_rate = 1/60.0
        # spawns snake randomly on the screen
        self.snake = Player(random.choice(listOfPoints)[0], random.choice(listOfPoints)[1], size, velocity)

    def on_draw(self):
        global rows, width
        self.clear()
        self.drawgrid(width, rows)
        self.snake.sprite.draw()



    def update(self, dt):
        self.snake.update()

# the player movement
    def on_key_press(self, symbol, modifier):
        if (symbol == key.RIGHT) or (symbol == key.D):
            # makes sure snake can only move in the lines (NEEDS TO BE FIXED)
            # should keep moving in the current direction until it can make the next possible turn
            tempList = [self.snake.sprite.x, self.snake.sprite.y]
            if tempList in listOfPoints:
                self.snake.vel_x = velocity
                self.snake.vel_y = 0
        elif (symbol == key.LEFT) or (symbol == key.A):
            tempList = [self.snake.sprite.x, self.snake.sprite.y]
            if tempList in listOfPoints:
                self.snake.vel_x = -velocity
                self.snake.vel_y = 0
        elif (symbol == key.UP) or (symbol == key.W):
            tempList = [self.snake.sprite.x, self.snake.sprite.y]
            if tempList in listOfPoints:
                self.snake.vel_y = velocity
                self.snake.vel_x = 0
        elif (symbol == key.DOWN) or (symbol == key.S):
            tempList = [self.snake.sprite.x, self.snake.sprite.y]
            if tempList in listOfPoints:
                self.snake.vel_y = -velocity
                self.snake.vel_x = 0
        # most recent key
        mrKey = symbol

# Draws Grid
    def drawgrid(self, width, rows):
        global size
        x = 0
        y = 0
        for i in range(rows):
            x = x + size
            y = y + size
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x, 0, x, width)))
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (0, y, width, y)))


if __name__ == "__main__":
    # sets rows adn width to global
    global rows, width, size, velocity, listOfPoints
    # size of screen
    width = 500
    # sets how many rows are in the grid (MUST be divisible by screen width)
    rows = 20
    # size of individual squares
    size = width // rows
    # speed of slithery boi
    velocity = 100
    # list of points (helps keep snake in grid)
    listOfPoints = []
    x = 0
    y = 0
    for i in range(rows):
        for j in range(rows):
            tempList = [x + ((width/rows) * i), y + ((width/rows) * j)]
            listOfPoints.append(tempList)

    window = GameWindow(width, width, "EPIC SNAKE GAME", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

