import tkinter as tk
import tkinter.ttk as ttk


def darkstyle():
    ''' Return a dark style '''
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style


root = tk.Tk()
root.title("My App")
root.resizable(False, False)
img = tk.PhotoImage(file="001.png")

style = darkstyle()


lab = ttk.Label(
    root,
    text="Hello World",
    compound="center",
    font="arial 50",
    image=img)
lab.pack(fill="both", expand=1)


button = ttk.Button(
    root,
    text="Click me",
    style="Accentbutton"
    )

button.place(relx=0.43, rely=0.7, width=100, height=30)


root.mainloop()
