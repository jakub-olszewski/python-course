import tkinter as tk  # Importowanie modułu tkinter, który umożliwia tworzenie interfejsu graficznego użytkownika (GUI).

a = {"admin": "123", "user": "haslo"}  # Słownik z danymi użytkowników i ich haseł.

class EntryRozszerzone(tk.Entry):
    # Klasa EntryRozszerzone dziedzicząca po tk.Entry, rozszerzająca funkcjonalność widgetu Entry.

    def __init__(self, master=None, tekst_zastepczy="podaj liczbe", color='grey'):
        super().__init__(master, width=26)  # Wywołanie konstruktora klasy bazowej Entry.

        self.tekst_zastepczy = tekst_zastepczy  # Tekst zastępczy, który jest wyświetlany w polu Entry, gdy jest puste.
        self.tekst_zastepczy_color = color  # Kolor tekstu zastępczego.
        self.default_fg_color = self['fg']  # Domyślny kolor tekstu.

        self.bind("<Key>", self.foc_in)  # Dodanie obsługi zdarzenia wciśnięcia klawisza.
        self.bind("<Leave>", self.foc_out)  # Dodanie obsługi zdarzenia opuszczenia widgetu.

        '''
        <Motion>: To zdarzenie występuje, gdy myszka jest przesuwana nad widgetem, 
        np. nad przyciskiem. Możesz użyć tego zdarzenia do wykrywania, 
        kiedy myszka znajduje się nad widgetem, co jest przydatne do 
        reagowania na ruch myszki nad obszarem widgetu.
        '''

        self.put_tekst_zastepczy()  # Wywołanie funkcji ustawiającej tekst zastępczy.

    def put_tekst_zastepczy(self):
        # Funkcja ustawiająca tekst zastępczy w polu Entry i zmieniająca kolor tekstu na kolor tekstu zastępczego.
        self.delete('0','end')  # Usunięcie aktualnej zawartości pola Entry.
        self.insert(0, self.tekst_zastepczy)  # Wstawienie tekstu zastępczego.
        self['fg'] = self.tekst_zastepczy_color  # Ustawienie koloru tekstu.

    def foc_in(self, *args):
        # Funkcja obsługująca zdarzenie wejścia na pole Entry (po kliknięciu na nie).
        if self['fg'] == self.tekst_zastepczy_color:  # Jeśli kolor tekstu jest równy kolorowi tekstu zastępczego.
            self.delete('0', 'end')  # Usunięcie tekstu zastępczego.
            self['fg'] = self.default_fg_color  # Przywrócenie domyślnego koloru tekstu.

    def foc_out(self, *args):
        # Funkcja obsługująca zdarzenie opuszczenia pola Entry (po wyjściu z niego).
        if not self.get():  # Jeśli pole Entry jest puste.
            self.put_tekst_zastepczy()  # Ustawienie tekstu zastępczego.

class Aplikacja:
    # Klasa Aplikacja, która tworzy interfejs użytkownika i obsługuje logikę logowania.

    def __init__(self, okno):
        self.tekst1 = tk.StringVar()  # Zmienna przechowująca tekst.

        self.label01 = tk.Label(okno, text="                    ")  # Tworzenie pustej etykiety.
        self.label01.grid(row=0, column=0)  # Umieszczenie etykiety w siatce (grid).

        self.label01 = tk.Label(okno, text="                    ")
        self.label01.grid(row=2, column=0)

        self.label01 = tk.Label(okno, text="                    ")
        self.label01.grid(row=4, column=0)

        self.label01 = tk.Label(okno, text="                    ")
        self.label01.grid(row=6, column=0)

        self.entry01 = EntryRozszerzone(okno, tekst_zastepczy="Podaj nazwę użytkownika")
        self.entry01.grid(row=1, column=1)  # Tworzenie pola Entry z tekstem zastępczym.

        self.entry02 = EntryRozszerzone(okno, tekst_zastepczy="Podaj hasło użytkownika")
        self.entry02.grid(row=3, column=1)  # Tworzenie pola Entry z tekstem zastępczym.

        self.b1 = tk.Button(okno, text="Zaloguj się", command=lambda: self.zmien_tekst(self.label01, self.entry01.get(), self.entry02.get()))
        self.b1.grid(row=5, column=1)  # Tworzenie przycisku "Zaloguj się" i przypisanie funkcji do jego kliknięcia.

        # pierwszy tekst
        self.label01 = tk.Label(okno, text="Czekam na zalogowanie")
        self.label01.grid(row=7, column=1)  # Tworzenie etykiety na komunikat o logowaniu.


    '''
    Linia pass jest pustą instrukcją w języku Python. Służy ona jako zastępcza lub placeholder,
    który nie wykonuje żadnych operacji. W tym przypadku, w funkcji zmien_tekst, linia pass jest tam
    jako tymczasowe miejsce na przyszłe dodatkowe operacje, które mogą być realizowane w tym miejscu,
    ale nie zostały jeszcze zaimplementowane.
    '''

    def zmien_tekst(self, label, user, passwd):
        # Funkcja sprawdzająca poprawność danych logowania i wyświetlająca odpowiedni komunikat.
        if user in a:  # Jeśli użytkownik istnieje w słowniku a.
            pass
            if passwd == a[user]:  # Jeśli hasło jest poprawne.
                label.config(text="Uzytkownik zalogowany")  # Zmiana tekstu na etykiecie na "Uzytkownik zalogowany".
            else:
                label.config(text="Złe hasło")  # Zmiana tekstu na etykiecie na "Złe hasło".
        else:
            label.config(text="Użytkownik nie istnieje")  # Zmiana tekstu na etykiecie na "Użytkownik nie istnieje".


okno = tk.Tk()  # Tworzenie głównego okna aplikacji.
okno.title("Moja apka - prosty system logowania")  # Ustawienie tytułu okna.
okno.geometry("300x400")  # Ustawienie rozmiaru okna.
okno.resizable(False, False)  # Wyłączenie możliwości zmiany rozmiaru okna.

app = Aplikacja(okno)  # Utworzenie obiektu klasy Aplikacja.

okno.mainloop()  # Uruchomienie głównej pętli aplikacji (event loop).
