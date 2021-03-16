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
        self.start_vx = 0
        self.start_vy = 0
        self.is_move = False

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

        self.start_vx = self.vx
        self.start_vy = self.vy

    def update(self):
        if self.is_move:
            self.x += 5
            self.y -= self.vy
            self.vy -= gravity

            if self.y > height:
                self.stop()
                self.hide()

    def start(self):
        self.show()
        self.is_move = True

    def stop(self):
        self.is_move = False

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vx = self.start_vx
        self.vy = self.start_vy
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
        if event.char == " ":
            if not self.banana.is_move:
                self.banana.reset()
                self.banana.start()

    def on_key_release(self, event):
        print("key release", event)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
    root.resizable(False, False)
    app = Monkey(root, width, height, delay)
    app.start()
    root.mainloop()
