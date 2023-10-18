import tkinter as tk
from tkinter import Menu

# Funkcja obsługująca przycisk "Say Hello"
def hello():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

# Funkcja obsługująca przycisk "Clear"
def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Funkcja do zamykania aplikacji
def quit_app():
    root.quit()

# Tworzenie głównego okna tkinter
root = tk.Tk()
root.title("Przykład 011")

# Tworzenie menu głównego
menubar = Menu(root)
root.config(menu=menubar)

# Tworzenie menu "Option"
option_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Opcje", menu=option_menu)
option_menu.add_command(label="Powiedz cześć", command=hello)
option_menu.add_command(label="Wyczyść", command=clear)
option_menu.add_separator()
option_menu.add_command(label="Wyjście", command=quit_app)

# Tworzenie etykiety i pola Entry
entry_label = tk.Label(root, text="Wprowadź swoje imię:")
entry_label.pack()  # Metoda pack() rozmieszcza elementy w oknie w sposób domyślny, od góry do dołu.

entry = tk.Entry(root)
entry.pack()  # Entry to pole tekstowe, które również umieszczamy w oknie za pomocą metody pack().

# Tworzenie przycisków
hello_button = tk.Button(root, text="Powiedz Cześć", command=hello)
hello_button.pack()  # Przycisk "Say Hello"

clear_button = tk.Button(root, text="Wyczyść", command=clear)
clear_button.pack()  # Przycisk "Clear"

# Etykieta do wyświetlania wyników
result_label = tk.Label(root, text="")
result_label.pack()

# Ustawienie początkowego rozmiaru okna
root.geometry("250x200")

# Rozpoczęcie głównej pętli tkinter
root.mainloop()
