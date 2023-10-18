import tkinter as tk
from tkinter import Menu

def hello():
    print("Hello!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Menu Example")

# Tworzenie menu głównego
menubar = Menu(root)
root.config(menu=menubar)

# Tworzenie menu "File"
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=hello)
file_menu.add_command(label="Save", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

# Tworzenie menu "Edit"
edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)

# Tworzenie menu "Help"
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=hello)

root.geometry("250x200")
root.mainloop()
