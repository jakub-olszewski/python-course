from tkinter import messagebox

# Wyświetlanie informacyjnego komunikatu
messagebox.showinfo("Tytuł", "To jest komunikat informacyjny.")

# Wyświetlanie komunikatu z pytaniem tak/nie
response = messagebox.askquestion("Pytanie", "Czy na pewno chcesz kontynuować?")
if response == "yes":
    print("Kontynuuj działanie.")
else:
    print("Anulowano.")