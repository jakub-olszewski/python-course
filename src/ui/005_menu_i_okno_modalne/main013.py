import tkinter as tk
from tkinter import messagebox


# Funkcja do walidacji wprowadzonych danych
def walidacja_dany_wejsciowych():
    # Pobieramy wprowadzone dane z pola Entry
    user_input = entry.get()

    # Sprawdzamy, czy pole Entry jest puste
    if not user_input:
        messagebox.showerror("Błąd", "Pole nie może być puste.")
    else:
        # Jeśli pole nie jest puste, wyświetlamy komunikat z wprowadzonym tekstem
        messagebox.showinfo("Informacja", f"Wprowadzono: {user_input}")


# Tworzenie głównego okna tkinter
root = tk.Tk()
root.title("Przykład walidacji")

# Tworzenie etykiety
label = tk.Label(root, text="Wprowadź jakąś informację:")
label.pack()

# Tworzenie pola Entry
entry = tk.Entry(root)
entry.pack()

# Tworzenie przycisku do walidacji
validate_button = tk.Button(root, text="Waliduj", command=walidacja_dany_wejsciowych)
validate_button.pack()

# Ustawienie początkowego rozmiaru okna
root.geometry("300x150")

# Rozpoczęcie głównej pętli tkinter
root.mainloop()
