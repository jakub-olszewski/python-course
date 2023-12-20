from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Tworzenie głównego okna
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Utworzenie tabeli
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        # Utworzenie formularza
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        # Dodawanie pól do formularza
        self.label1 = QLabel("Numer szafy:")
        self.lineEdit1 = QLineEdit()
        self.formLayout.addRow(self.label1, self.lineEdit1)

        self.label2 = QLabel("Numer laptopa:")
        self.lineEdit2 = QLineEdit()
        self.formLayout.addRow(self.label2, self.lineEdit2)

        self.label3 = QLabel("Numer identyfikacyjny:")
        self.lineEdit3 = QLineEdit()
        self.formLayout.addRow(self.label3, self.lineEdit3)

        self.label4 = QLabel("Marka:")
        self.lineEdit4 = QLineEdit()
        self.formLayout.addRow(self.label4, self.lineEdit4)

        self.label5 = QLabel("Model:")
        self.lineEdit5 = QLineEdit()
        self.formLayout.addRow(self.label5, self.lineEdit5)

        self.label6 = QLabel("Osoba pobierająca:")
        self.lineEdit6 = QLineEdit()
        self.formLayout.addRow(self.label6, self.lineEdit6)

        self.label7 = QLabel("Stan:")
        self.lineEdit7 = QLineEdit()
        self.formLayout.addRow(self.label7, self.lineEdit7)

        self.verticalLayout.addLayout(self.formLayout)

        # Przyciski do dodawania, edycji i usuwania
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.addButton = QPushButton("Dodaj")
        self.editButton = QPushButton("Edytuj")

        self.horizontalLayout.addWidget(self.addButton)
        self.horizontalLayout.addWidget(self.editButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Ustawienie centralnego widgetu w głównym oknie
        MainWindow.setCentralWidget(self.centralwidget)

        # Tłumaczenie etykiet i ustawianie tytułu okna
        self.retranslateUi(MainWindow)

    # retranslateUi to metoda, która jest generowana automatycznie przez Qt Designer
    # podczas tworzenia interfejsu użytkownika w programie Qt.
    # Jest ona używana do ustawienia tekstu dla różnych elementów interfejsu,
    # takich jak etykiety, przyciski, itp. w zależności od aktualnie ustawionego języka.
    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja do pobierania laptopów szkolnych"))
        self.label1.setText(_translate("MainWindow", "Numer szafy:"))
        self.label2.setText(_translate("MainWindow", "Numer laptopa:"))
        self.label3.setText(_translate("MainWindow", "Numer identyfikacyjny:"))
        self.label4.setText(_translate("MainWindow", "Marka:"))
        self.label5.setText(_translate("MainWindow", "Model:"))
        self.label6.setText(_translate("MainWindow", "Osoba pobierająca:"))
        self.label7.setText(_translate("MainWindow", "Stan:"))

# Klasa aplikacji
class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inicjalizacja danych
        self.data = []

        # Podłączanie przycisków do funkcji obsługi zdarzeń
        self.addButton.clicked.connect(self.add_entry)
        self.editButton.clicked.connect(self.edit_entry)

        # Wypełnienie tabeli przykładowymi danymi
        self.populate_table()

    # populate_table to metoda, która wypełnia tabelę (QTableWidget)
    # danymi znajdującymi się w atrybucie self.data. Aby to zrobić,
    # najpierw ustawia nagłówki kolumn tabeli na podstawie listy headers,
    # a następnie wypełnia poszczególne komórki danymi z listy self.data.
    def populate_table(self):
        headers = ["Numer szafy", "Numer laptopa", "Numer identyfikacyjny", "Marka", "Model", "Osoba pobierająca", "Stan"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, entry in enumerate(self.data):
            for col, value in enumerate(entry):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

    def add_entry(self):
        # Dodawanie nowego wpisu
        self.clear_form()

    def edit_entry(self):
        # Edycja zaznaczonego wpisu
        current_row = self.tableWidget.currentRow()

        if current_row == -1:
            QMessageBox.warning(self, "Błąd", "Wybierz wpis do edycji.")
            return

        # Wypełnienie formularza danymi z zaznaczonego wpisu
        entry = self.data[current_row]
        self.lineEdit1.setText(entry[0])




if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()
