class Ptak:

    def __init__(self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość

    def lec(self):
        print("Tu", self.gatunek, ". Startuje, i zaraz osiągne prędkość", self.szybkość)

    def wydajOdglos(self):
        '''
        W przypadku, który przedstawiłeś, pass zostało użyte jako zastępcza lub placeholder w metodzie wydajOdglos().
        To oznacza, że ta metoda nie zawiera jeszcze żadnej konkretnej implementacji, ale została zdefiniowana w klasie.

        Przykładem sytuacji, w której pass może być używane, to wtedy,
        gdy planuje się późniejszą implementację danej metody lub funkcji, ale aktualnie nie ma jeszcze jasnej koncepcji,
        co ta metoda ma robić. Pozwala to na zdefiniowanie interfejsu lub struktury kodu,
        a następnie późniejsze uzupełnienie go konkretną logiką.
        '''
        pass


class Orzel(Ptak):

    def poluj(self):
        print("Tu", self.gatunek, ". Rozpoczołem polowanie")


class Pingwin(Ptak):

    def slizgaj(self):
        print("Tu", self.gatunek, ". Rozpoczołem ślizg")

    def lec(self):
        print("Tu", self.gatunek, ". Przykro mi, ale nie latam")


# Tworzenie obiektów
ptak = Ptak("Nieznany",140)
orzel = Orzel("Orzeł", 100)
pingwin = Pingwin("Pingwin", 10)

# Wywołanie metody lec na obiektach
orzel.lec()  # Wynik: Tu Orzeł . Startuję, i zaraz osiągnę prędkość 100
pingwin.lec()  # Wynik: Tu Pingwin . Przykro mi, ale nie latam

# Wywołanie metody poluj tylko na obiekcie Orzel
orzel.poluj()  # Wynik: Tu Orzeł . Rozpocząłem polowanie

# Wywołanie metody slizgaj tylko na obiekcie Pingwin
pingwin.slizgaj()  # Wynik: Tu Pingwin . Rozpocząłem ślizg

ptak.lec()

