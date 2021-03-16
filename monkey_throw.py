import tkinter as tk
from gamelib import Sprite, GameApp

width = 800
height = 500
delay = 33
gravity = 1


class Banana(Sprite):
    def init_sprite(self):
        self.vx = 0
        self.vy = 0

        self.start_x = self.x
        self.start_y = self.y
        self.is_move = False

        self.hide()

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def update(self):
        if self.is_move:
            self.x += 5
            self.y -= self.vy
            self.vy -= gravity

    def start(self):
        self.is_move = True

    def stop(self):
        self.is_move = False

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.stop()


class Monkey(GameApp):
    def init_game(self):
        self.create_sprite()

    def create_sprite(self):
        self.banana = Banana(self, "banana.png", 100, 400)
        self.banana.set_speed(15, 25)

        self.monkey = Sprite(self, "monkey.png", 100, 400)
        self.enemy = Sprite(self, "monkey.png", 700, 400)

        self.sprite.append(self.banana)
        self.sprite.append(self.monkey)
        self.sprite.append(self.enemy)

    def on_key_press(self, event):
        print("key press", event)

    def on_key_release(self, event):
        print("key release", event)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
    root.resizable(False, False)
    app = Monkey(root, width, height, delay)
    app.start()
    root.mainloop()
