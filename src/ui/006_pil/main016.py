import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Example image")

# Otwieranie obrazu przy użyciu Pillow
img = Image.open("example.jpg")

# Konwertowanie obrazu do formatu ImageTk
img_tk = ImageTk.PhotoImage(img)

# Wyświetlanie obrazu w oknie Tkinter
label = tk.Label(root, image=img_tk)
label.pack()

root.mainloop()
