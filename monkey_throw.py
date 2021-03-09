import tkinter as tk
import tkinter.ttk as ttk

width = 800
height = 500


class Monkey(tk.Frame):
    def __init__(self, parents):
        super().__init__(parents)
        self.grid(sticky="news")
        self.create_widget()

    def create_widget(self):
        self.cavas = tk.Canvas(self, borderwidth=0, width=width, height=height, highlightthickness=0)
        self.cavas.grid(sticky="news")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
    root.resizable(False, False)
    app = Monkey(root)
    root.mainloop()