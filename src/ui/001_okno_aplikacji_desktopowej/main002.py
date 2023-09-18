import tkinter

okno = tkinter.Tk()

# dodanie nazwy okna
okno.title("Moja aplikacja desktopowa")

# dodanie wymiarów okna
okno.geometry("480x640")

# zablokowanie skalowania okna
okno.resizable(False, False)

okno.mainloop()
