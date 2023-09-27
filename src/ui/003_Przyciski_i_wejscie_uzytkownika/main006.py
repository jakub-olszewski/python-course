# Funkcja lambda w Pythonie to funkcja anonimowa, czyli funkcja bez nazwy.
# Jest to krótka forma zapisu funkcji, która może być używana w miejscu,
# gdzie oczekiwana jest funkcja, np. jako argument innej funkcji.
# Funkcje lambda są często używane do tworzenia małych funkcji jednolinijkowych.
#
# Składnia funkcji lambda jest następująca:
#
# lambda argumenty: wyrażenie
#
# * lambda to słowo kluczowe rozpoczynające definicję funkcji lambda.
# * argumenty to lista argumentów, które funkcja lambda może przyjmować (może być ich zero lub więcej).
# * wyrażenie to jedno wyrażenie, które jest wynikiem działania funkcji. Wynik tego wyrażenia jest zwracany przez funkcję lambda.



# Definicja funkcji lambda, która dodaje dwa argumenty
dodaj = lambda x, y: x + y

# Wywołanie funkcji lambda
wynik = dodaj(3, 5)  # Wynik to 8

# Wypisanie wyniku na konsoli
print(wynik)