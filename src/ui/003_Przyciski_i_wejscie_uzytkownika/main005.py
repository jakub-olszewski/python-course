import tkinter as tk

# Klasa używająca frameworka GUI Tkinter
class Aplikacja:
    # Konstruktor klasy, pobieranie elementu okna
    def __init__(self, okno):
        # Inicjalizacja zmiennej do przechowywania tekstu
        self.tekst = tk.StringVar()
        self.tekst.set("Witaj")

        # Utworzenie etykiety z tekstem
        self.label01 = tk.Label(okno, textvariable=self.tekst)
        self.label01.grid(row=0, column=0)  # Umieszczenie etykiety w oknie

        # Utworzenie przycisku nr 1
        self.b1 = tk.Button(okno, text="Przycisk nr 1", command=self.zmien_tekst)
        self.b1.grid(row=0, column=1)  # Umieszczenie przycisku nr 1 w oknie

        # Utworzenie drugiej etykiety z tekstem
        self.label02 = tk.Label(okno, text="Zmień mnie")
        self.label02.grid(row=1, column=0)  # Umieszczenie drugiej etykiety w oknie

        # Utworzenie przycisku nr 2
        self.b2 = tk.Button(okno, text="Przycisk nr 2", command=lambda : self.zmien_tekst_w(self.label02))
        self.b2.grid(row=1, column=1)  # Umieszczenie przycisku nr 2 w oknie

    # Metoda zmieniająca tekst przy użyciu przycisku nr 1
    def zmien_tekst(self):
        self.tekst.set("Tekst został zmieniony")

    # Metoda zmieniająca tekst w drugiej etykiecie przy użyciu przycisku nr 2
    def zmien_tekst_w(self, label):
        label.config(text="Tekst został zmieniony 2")

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Przykład 005")
okno.geometry("300x400")  # Ustawienie rozmiaru okna
okno.resizable(False, False)  # Zablokowanie skalowania okna
app = Aplikacja(okno)  # Inicjalizacja aplikacji
okno.mainloop()  # Uruchomienie głównej pętli aplikacji
