from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QGridLayout

class MainWindow(QMainWindow):
    """
    Fenêtre principale de l'application.

    Cette classe représente la fenêtre principale de l'application. Elle comprend une disposition en grille avec une étiquette, 
    une ligne d'édition pour l'entrée du nom, un bouton 'Ok' pour afficher un message de bienvenue, et un bouton 'Quitter' pour quitter l'application.
    """

    def __init__(self):
        """
        Initialise MainWindow.

        Cette méthode initialise la MainWindow, met en place les widgets et connecte les signaux.
        """
        super().__init__()
        
        widget = QWidget ()
        self.setCentralWidget(widget)
        
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        
        lab = QLabel("Saisir votre nom")
        self.__nom = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

        self.__grid.addWidget(lab, 0, 0, 1, 3)
        self.__grid.addWidget(self.__nom, 1, 0, 1, 3)
        self.__grid.addWidget(ok, 2, 1, 1, 1)
        self.__grid.addWidget(quit, 4, 1, 1, 1)

        ok.clicked.connect(self.__actionok)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Hello world")


    def __actionok(self):
        """
        Gère le clic sur le bouton 'Ok'.

        Cette méthode est appelée lorsque le bouton 'Ok' est cliqué. Elle crée une nouvelle étiquette avec un message de bienvenue et l'ajoute à la disposition en grille.
        """
        lab_ok = QLabel(f"Bonjour {self.__nom.text()}")
        self.__grid.addWidget(lab_ok, 3, 0, 1, 3)
    
    def __actionQuitter(self):
        """
        Gère le clic sur le bouton 'Quitter'.

        Cette méthode est appelée lorsque le bouton 'Quitter' est cliqué. Elle quitte l'application.
        """
        QApplication.exit(0)