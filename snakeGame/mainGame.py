import pyglet
from Snake import Player
from pyglet.window import key
import random

#create the game window
class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(100, 200)
        self.frame_rate = 1/60.0

        self.snake = Player(random.randint(50, 450), random.randint(50, 450), 20, 20)

    def on_draw(self):
        self.clear()
        self.snake.sprite.draw()

    def update(self, dt):
        self.snake.update()

#the player movement
    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.snake.vel_x = 130
            self.snake.vel_y = 0
        elif symbol == key.LEFT:
            self.snake.vel_x = -130
            self.snake.vel_y = 0
        elif symbol == key.UP:
            self.snake.vel_y = 130
            self.snake.vel_x = 0
        elif symbol == key.DOWN:
            self.snake.vel_y = -130
            self.snake.vel_x = 0


if __name__ == "__main__":
    window = GameWindow(500, 500, "EPIC SNAKE GAME", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

