import tkinter as tk

okno = tk.Tk()

# dodanie nazwy okna
okno.title("Aplikacja desktopowa")

# dodanie wymiarów okna
okno.geometry("300x400")

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

okno.mainloop()
