import tkinter as tk

# Klasa używająca frameworka GUI Tkinter
class Aplikacja:
    # Konstruktor klasy, pobieranie elementu okna
    def __init__(self, okno):
        # utworzenie zmiennych tekstowych
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()
        # zwykly tekst
        self.label01 = tk.Label(okno, text="Podaj liczbe")
        self.label01.grid(row=0, column=0)

        # wejście od uzytkownika
        self.entry01 = tk.Entry(okno, textvariable=self.tekst1, font=('none', 9, ' italic '))
        # ustawienie nowego entry na miejscu
        self.entry01.grid(row=0, column=1)

        # Dodanie przycisku z wywolaniem metody
        self.b1 = tk.Button(okno, text="Przekaż liczbę", command=lambda: self. zmien_tekst(self.label03, self.tekst1, "Podana liczba:"))
        self.b1.grid(row=0, column=2)

        # zwykly tekst
        self.label02 = tk.Label(okno, text="Podaj hasło")
        self.label02.grid(row=1, column=0)

        # drugie wejscie tekstowe, tym razem z ukrytym wpisywaniem
        self.entry02 = tk.Entry(okno, textvariable=self.tekst2, show="*")
        # ustawienie nowego tekstu na miejscu
        self.entry02.grid(row=1, column=1)

        # Dodanie przycisku z •wywolaniem metody
        self.b2 = tk.Button(okno, text="Przekaż hasło", command=lambda: self. zmien_tekst(self.label04, self.tekst2, "Hasło to: "))
        self.b2.grid(row=1, column=2)

        # trzeci tekst
        self.label03 = tk.Label(okno, text="Zmień mnie")
        self.label03.grid(row=2, column=1)

        # czwarty tekst
        self.label04 = tk.Label(okno, text="Hasło to")
        self.label04.grid(row=3, column=1)

        # Dodanie przycisku czerwonego
        self.color_button = tk.Button(okno, text="ZSE", fg="#D7BFDC", bg="#7F00FF", font=("Comic Sans", 16, "italic"))
        self.color_button.grid(row=4, column=1)

    def zmien_tekst(self, label, textvar, text):
        label.config(text=(str(text)+ str(textvar.get())))

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Przykład 007")
okno.geometry("300x400")  # Ustawienie rozmiaru okna
okno.resizable(False, False)  # Zablokowanie skalowania okna

app = Aplikacja(okno)  # Inicjalizacja aplikacji

okno.mainloop()  # Uruchomienie głównej pętli aplikacji