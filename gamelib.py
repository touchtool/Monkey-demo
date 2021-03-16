import tkinter as tk


class GameApp(tk.Frame):
    def __init__(self, parents, cavas_width=800, canvas_height=500, delay=33):
        super().__init__(parents)
        self.canvas_width = cavas_width
        self.canvas_height = canvas_height

        self.delay = delay

        self.grid(sticky="news")
        self.create_canvas()

        self.sprite = []
        self.init_game()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, borderwidth=0, width=self.canvas_width, height=self.canvas_height, highlightthickness=0)
        self.canvas.grid(sticky="news")

    def animate(self):
        self.banana.update()
        self.banana.render()
        self.after(self.delay, self.animate)

    def start(self):
        self.after(0, self.animate)


class Sprite:
    def __init__(self, game_app, image_file, x=0, y=0):
        self.image_file = image_file
        self.canvas = game_app.canvas
        self.x = x
        self.y = y

        self.init_canvas_object()
        self.init_sprite()

    def init_sprite(self):
        pass

    def init_canvas_object(self):
        self.photo_img = tk.PhotoImage(file=self.image_file)
        self.canvas_object_id = self.canvas.create_image(self.x, self.y, image=self.photo_img)

    def render(self):
        self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def update(self):
        pass

