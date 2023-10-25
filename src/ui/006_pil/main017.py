from tkinter import Tk, Menu, messagebox, filedialog, Label
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
    if file_path:
        try:
            with Image.open(file_path) as image:
                width, height = image.size
                format = image.format
                mode = image.mode
                info = f"Informacje o pliku:\n\n"
                info += f"Ścieżka pliku: {file_path}\n"
                info += f"Rozmiar obrazu: {width} x {height} pikseli\n"
                info += f"Format: {format}\n"
                info += f"Tryb: {mode}\n"

                # Wyświetl obrazek w oknie aplikacji
                img = ImageTk.PhotoImage(image)
                image_label.config(image=img)
                image_label.photo = img

                messagebox.showinfo("Informacje o pliku", info)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można otworzyć pliku: {str(e)}")

root = Tk()
root.title("Otwieranie i wyświetlanie informacji o pliku")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Otwórz obraz", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Wyjście", command=root.quit)

image_label = Label(root)
image_label.pack()

root.mainloop()
