import tkinter as tk
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Erstelle einen Regler (Scale) und setze seine Eigenschaften
        self.slider = tk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL, command=self.update_progress)
        self.slider.pack()

        # Erstelle einen Ladebalken (Progressbar) und setze seine Eigenschaften
        import tkinter.ttk as ttk
        self.progressbar = tk.ttk.Progressbar(self, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progressbar.pack()

    def update_progress(self, value):
        # Aktualisiere den Fortschrittsbalken basierend auf dem Reglerwert
        self.progressbar['value'] = float(value)

root = tk.Tk()
app = App(master=root)
app.mainloop()
