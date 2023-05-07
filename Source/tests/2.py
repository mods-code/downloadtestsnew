from tkinter import ttk
from ttkthemes import ThemedTk

# Erstelle ein ThemedTk-Fenster mit dem "plastik" Theme
root = ThemedTk(theme="plastik")

# Setze den Fenstertitel
root.title("TTK Themes Beispiel")

# Erstelle ein Label-Widget
label = ttk.Label(root, text="Hallo Welt!")
label.pack(padx=10, pady=10)

# Starte die Hauptschleife
root.mainloop()
