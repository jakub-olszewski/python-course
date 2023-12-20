# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main051xKFjtv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Importowanie niezbędnych modułów z PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(270, 104)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        # Label i QLineEdit dla pola "Login"
        self.labelLogin = QLabel(self.centralwidget)
        self.labelLogin.setObjectName(u"labelLogin")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelLogin)
        self.lineEditLogin = QLineEdit(self.centralwidget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditLogin)

        # Label i QLineEdit dla pola "Password"
        self.labelPassword = QLabel(self.centralwidget)
        self.labelPassword.setObjectName(u"labelPassword")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QLineEdit(self.centralwidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditPassword)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QVBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # Przycisk "Zaloguj"
        self.pushButtonLogin = QPushButton(self.centralwidget)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)

        # Przycisk "Zarejestruj"
        self.pushButtonRegister = QPushButton(self.centralwidget)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")
        self.horizontalLayout.addWidget(self.pushButtonRegister)

        self.verticalLayout.addLayout(self.horizontalLayout)

        LoginWindow.setCentralWidget(self.centralwidget)

        # Ustawienia interfejsu użytkownika
        self.retranslateUi(LoginWindow)

        # Połączenie sygnału kliknięcia przycisku "Zaloguj" z funkcją login
        QMetaObject.connectSlotsByName(LoginWindow)
        self.pushButtonLogin.clicked.connect(self.login)

    def retranslateUi(self, LoginWindow):
        # Tłumaczenie napisów wyświetlanych w interfejsie użytkownika
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login Window", None))
        self.labelLogin.setText(QCoreApplication.translate("LoginWindow", u"Login:", None))
        self.labelPassword.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("LoginWindow", u"Zaloguj", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("LoginWindow", u"Zarejestruj", None))

    def login(self):
        # Funkcja obsługująca logowanie
        login = self.lineEditLogin.text()
        password = self.lineEditPassword.text()

        # Sprawdzenie, czy dane logowania są poprawne
        if login == "admin" and password == "admin":
            QMessageBox.information(self.centralwidget, "Logowanie", "Pomyślnie zalogowano!")
        else:
            QMessageBox.warning(self.centralwidget, "Błąd logowania", "Nieprawidłowe dane logowania.")


# Inicjalizacja aplikacji Qt
app = QApplication([])

# Stworzenie okna głównego
MainWindow = QtWidgets.QMainWindow()

# Stworzenie obiektu klasy Ui_LoginWindow
ui = Ui_LoginWindow()

# Konfiguracja interfejsu użytkownika
ui.setupUi(MainWindow)

# Wyświetlenie okna głównego
MainWindow.show()

# Rozpoczęcie głównej pętli programu
app.exec()
