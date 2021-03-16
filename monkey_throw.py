import tkinter as tk
import tkinter.ttk as ttk

width = 800
height = 500
delay = 33
gravity = 1


class Sprite():
    def __init__(self, canvas, image_file, x=0, y=0):
        self.image_file = image_file
        self.canvas = canvas
        self.x = x
        self.y = y

        self.init_canvas_object()

    def init_sprite(self):
        pass

    def init_canvas_object(self):
        self.photo_img = tk.PhotoImage(file=self.image_file)
        self.canvas_object_id = self.canvas.create_image(self.x, self.y, image=self.photo_img)

    def render(self):
        self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def update(self):
        pass


class Banana(Sprite):
    def init_sprite(self):
        self.vx = 0
        self.vy = 0

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += 5
        self.y -= self.vy
        self.vy -= gravity


class Monkey(tk.Frame):
    def __init__(self, parents):
        super().__init__(parents)
        self.grid(sticky="news")
        self.create_widget()
        self.create_sprite()

    def create_widget(self):
        self.canvas = tk.Canvas(self, borderwidth=0, width=width, height=height, highlightthickness=0)
        self.canvas.grid(sticky="news")


    def create_sprite(self):
        self.banana = Banana(self.canvas, "banana.png", 100, 100)
        self.banana.set_speed(10, 20)

    def animate(self):
        self.banana.update()
        self.banana.render()
        self.after(delay, self.update)

    def start(self):
        self.after(0, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
    root.resizable(False, False)
    app = Monkey(root)
    app.start()
    root.mainloop()
