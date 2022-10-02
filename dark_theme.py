
import tkinter as tk
import tkinter.ttk as ttk
import azure_dark

def main_window():
    """ The window with the darkstyle """
    root = tk.Tk()
    azure_dark.apply_theme(root)

    root.title("My App")
    root.resizable(False, False)
    img = tk.PhotoImage(file="001.png")

    lab = ttk.Label(
        root,
        text="Hello World",
        compound="center",
        font="arial 50",
        image=img
    )
    lab.pack(fill="both", expand=1)

    b = tk.BooleanVar()
    for widget in [
        ttk.Button(root, text="Button 1", style="Accentbutton"),
        ttk.Button(root, text="Button 2"),
        ttk.Button(root, text="Button 3"),
        ttk.Button(root, text="Button 4"),
        ttk.Checkbutton(root, text='Checkbutton 1', variable=b                      ),
        ttk.Checkbutton(root, text='Checkbutton 2', variable=b, style='Togglebutton'),
        ttk.Checkbutton(root, text='Checkbutton 3', variable=b, style='Switch'      ),
    ]: widget.pack()

    root.mainloop()

main_window()
