import tkinter as tk
from tkinter import simpledialog


# Funkcja do otwierania okna modalnego
def open_modal_dialog():
    # Wywołujemy simpledialog.askstring(), aby poprosić użytkownika o wprowadzenie tekstu.
    # Parametr "Okno modalne" to tytuł okna modalnego, a "Podaj swoje imię:" to treść pytania.
    result = simpledialog.askstring("Okno modalne", "Podaj swoje imię:")

    # Sprawdzamy, czy użytkownik wprowadził tekst i czy nie kliknął przycisku "Anuluj".
    if result:
        # Jeśli użytkownik wprowadził tekst, aktualizujemy etykietę z odpowiedzią.
        label.config(text=f"Witaj, {result}!")


# Tworzenie głównego okna tkinter
root = tk.Tk()
root.title("Przykład okna modalnego")

# Tworzenie przycisku do otwierania okna modalnego
button = tk.Button(root, text="Otwórz okno modalne", command=open_modal_dialog)
button.pack()  # Przycisk umieszczamy w oknie głównym za pomocą metody pack().

# Etykieta do wyświetlania powitania
label = tk.Label(root, text="")
label.pack()  # Etykietę również umieszczamy w oknie głównym za pomocą metody pack().

# Ustawienie początkowego rozmiaru okna
root.geometry("300x100")

# Rozpoczęcie głównej pętli tkinter
root.mainloop()
