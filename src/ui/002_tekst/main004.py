import tkinter as tk

okno = tk.Tk()

# dodanie nazwy okna
okno.title("Aplikacja desktopowa")

# dodanie wymiarów okna
okno.geometry("600x300")

# zablokowanie skalowania okna
okno.resizable(False, False)

tekst = tk.StringVar()

tekst.set("Programowanie aplikacji desktopowych")

# zwykły tekst
label01 = tk.Label(okno, textvariable=tekst)

# ustawienie nowego tekstu na miejscu
label01.grid(row=0, column=0)

# zmiana kolorów tekstu i tła
label02 = tk.Label(okno, textvariable=tekst, bg="black", fg="white")
label02.grid(row=1, column=0)

# zmiana kolorów tekstu i tła za pomocą kolorów zapisanych hexadecymalnie
label03 = tk.Label(okno, textvariable=tekst, bg="#ff0000", fg="#00ff00")
label03.grid(row=2, column=0)

# zmiana wielkości i pogrubienie tekstu
label04 = tk.Label(okno, textvariable=tekst, font="none 16 bold")
label04.grid(row=3, column=0)

# dodanie systemowego fontu i ustawienie pochyłej kursywy tekstu
label05 = tk.Label(okno, textvariable=tekst, font=("Times New Roman", 16, "italic"))

label05.grid( row=4, column=0)

okno. mainloop()


okno.mainloop()
