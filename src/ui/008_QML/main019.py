import sys
from PyQt6 import QtQml
from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtQml import QQmlApplicationEngine

# Klasa Backend dziedzicząca po QObject
class Backend(QObject):
    # Sygnał informujący o zmianie tekstu
    textChanged = pyqtSignal(str)

    # Konstruktor klasy Backend
    def __init__(self, parent=None):
        super(Backend, self).__init__(parent)
        self._text = ""

    # Deklaracja właściwości text z powiadomieniem o zmianie
    @pyqtProperty(str, notify=textChanged)
    def text(self):
        return self._text

    # Setter dla właściwości text, emituje sygnał o zmianie
    @text.setter
    def text(self, value):
        print(f"type {self.text}")
        if self._text != value:
            self._text = value
            self.textChanged.emit(value)

    # Slot do wyświetlania MessageBox z tekstem "Hello, {self.text}!"
    @pyqtSlot()
    def showMessage(self):
        print("click showMessage")
        message = f"Hello, {self.text}!"
        QMessageBox.information(None, "Informacja", message)

# Początek kodu, który wykonuje się tylko przy bezpośrednim uruchomieniu skryptu
if __name__ == "__main__":
    # Inicjalizacja obiektu QGuiApplication
    app = QApplication(sys.argv)

    # Inicjalizacja obiektu QQmlApplicationEngine do obsługi QML
    myEngine = QtQml.QQmlApplicationEngine()

    # Utworzenie obiektu klasy Backend
    backend = Backend()

    # Załaduj plik QML
    myEngine.load("main019.qml")

    # Zarejestruj obiekt Pythona w kontekście QML jako "backend"
    myEngine.rootContext().setContextProperty("backend", backend)

    # Sprawdź, czy załadowano obiekty z pliku QML
    if not myEngine.rootObjects():
        sys.exit(-1)

    # Uruchom pętlę główną aplikacji PyQt
    sys.exit(app.exec())
