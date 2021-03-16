import tkinter as tk


class GameApp(tk.Frame):
    def __init__(self, parent, cavas_width=800, canvas_height=500, delay=33):
        super().__init__(parent)
        self.parent = parent
        self.canvas_width = cavas_width
        self.canvas_height = canvas_height

        self.delay = delay

        self.grid(sticky="news")
        self.create_canvas()

        self.parent.bind("<KeyPress>", self.on_key_press)
        self.parent.bind("<KeyRelease>", self.on_key_release)

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

    def on_key_press(self):
        pass

    def on_key_release(self):
        pass


class Sprite:
    def __init__(self, game_app, image_file, x=0, y=0):
        self.image_file = image_file
        self.canvas = game_app.canvas
        self.x = x
        self.y = y

        self.is_visible = True

        self.init_canvas_object()
        self.init_sprite()

    def init_sprite(self):
        pass

    def init_canvas_object(self):
        self.photo_img = tk.PhotoImage(file=self.image_file)
        self.canvas_object_id = self.canvas.create_image(self.x, self.y, image=self.photo_img)

    def render(self):
        if self.is_visible:
            self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def show(self):
        self.is_visible = True
        self.canvas.itemconfigure(self.canvas_object_id, state="normal")

    def hide(self):
        self.is_visible = False
        self.canvas.itemconfigure(self.canvas_object_id, state="hidden")

    def update(self):
        pass

