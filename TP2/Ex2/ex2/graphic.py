from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QGridLayout, QComboBox

class MainWindow(QMainWindow):
    """
    Classe principale de l'application de conversion de température.

    Cette classe crée une interface utilisateur pour convertir les températures entre les degrés Celsius, Kelvin et Fahrenheit.

    Attributes
    ----------
    __lab2 : QLabel
        Label pour afficher l'unité de température d'entrée.
    __lab4 : QLabel
        Label pour afficher l'unité de température de sortie.
    __error : QLabel
        Label pour afficher les messages d'erreur.
    __temp : QLineEdit
        Champ de texte pour l'entrée de la température.
    __result : QLineEdit
        Champ de texte pour afficher le résultat de la conversion.
    __selector : QComboBox
        Sélecteur pour choisir le type de conversion.

    Methods
    -------
    __update_label():
        Met à jour les labels d'unité en fonction du type de conversion sélectionné.
    __action_convertir():
        Convertit la température entrée en fonction du type de conversion sélectionné.
    __action_aide():
        Ouvre une nouvelle fenêtre avec des informations d'aide.
    """

    def __init__(self):
        """
        Construit tous les widgets nécessaires et les ajoute à la fenêtre principale.
        """
        super().__init__()
        
        widget = QWidget ()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        lab = QLabel("Température")
        self.__lab2 = QLabel("")
        lab3 = QLabel("Conversion")
        self.__lab4 = QLabel("")
        self.__error = QLabel("")

        self.__temp = QLineEdit("")

        self.__result = QLineEdit("")
        self.__result.setReadOnly(True)


        self.__selector = QComboBox()
        self.__selector.addItem("°C -> °K")
        self.__selector.addItem("°C -> °F")
        
        self.__selector.addItem("°K -> °C")
        self.__selector.addItem("°K -> °F")
        
        self.__selector.addItem("°F -> °C")
        self.__selector.addItem("°F -> °K")

        self.__selector.setCurrentIndex(0)
        self.__update_label()
            

        convertir = QPushButton("Convertir")
        aide = QPushButton("?")


        grid.addWidget(lab, 0, 0, 1, 1)
        grid.addWidget(self.__temp, 0, 1, 1, 1)
        grid.addWidget(self.__lab2, 0, 2, 1, 1)

        grid.addWidget(self.__error, 1, 0, 1, 3)

        grid.addWidget(convertir, 2, 1, 1, 1)
        grid.addWidget(self.__selector, 2, 2, 1, 1)

        grid.addWidget(lab3, 3, 0, 1, 1)
        grid.addWidget(self.__result, 3, 1, 1, 1)
        grid.addWidget(self.__lab4, 3, 2, 1, 1)

        grid.addWidget(aide, 4, 4, 1, 1)


        self.__selector.currentIndexChanged.connect(self.__update_label)

        convertir.clicked.connect(self.__action_convertir)
        aide.clicked.connect(self.__action_aide)

        self.setWindowTitle("Conversion de Température")


    def __update_label(self):
        """
        Met à jour les labels d'unité en fonction du type de conversion sélectionné dans le sélecteur.
        """
        if self.__selector.currentIndex() == 0:
            self.__lab2.setText("°C")
            self.__lab4.setText("°K")
        elif self.__selector.currentIndex() == 1:
            self.__lab2.setText("°C")
            self.__lab4.setText("°F")
        elif self.__selector.currentIndex() == 2:
            self.__lab2.setText("°K")
            self.__lab4.setText("°C")
        elif self.__selector.currentIndex() == 3:
            self.__lab2.setText("°K")
            self.__lab4.setText("°F")
        elif self.__selector.currentIndex() == 4:
            self.__lab2.setText("°F")
            self.__lab4.setText("°C")
        elif self.__selector.currentIndex() == 5:
            self.__lab2.setText("°F")
            self.__lab4.setText("°K")


    def __action_convertir(self):
        """
        Convertit la température entrée en fonction du type de conversion sélectionné.
        Si la température entrée n'est pas un nombre valide, affiche un message d'erreur.
        """
        try:
            if self.__temp.text() == "":
                raise ValueError
            
            temp = float(self.__temp.text())
            if self.__selector.currentIndex() == 0 and temp >= -273.15:
                conv = temp + 273.15
                self.__result.setText(f"{conv:.2f}")
            elif self.__selector.currentIndex() == 1 and temp >= -273.15:
                conv = temp * 9/5 + 32
                self.__result.setText(f"{conv:.2f}")
            elif self.__selector.currentIndex() == 2 and temp >= 0:
                conv = temp - 273.15
                self.__result.setText(f"{conv:.2f}")
            elif self.__selector.currentIndex() == 3 and temp >= 0:
                conv = (temp - 273.15) * 9/5 + 32
                self.__result.setText(f"{conv:.2f}")
            elif self.__selector.currentIndex() == 4 and temp >= -459.67:
                conv = (temp - 32) * 5/9
                self.__result.setText(f"{conv:.2f}")
            elif self.__selector.currentIndex() == 5 and temp >= -459.67:
                conv = (temp - 32) * 5/9 + 273.15
                self.__result.setText(f"{conv:.2f}")
            else:
                raise ValueError
            
        except ValueError:
            self.__error.setText(f"{self.__temp.text()}{self.__lab2} n'est pas un nombre valide")


    def __action_aide(self):
        """
        Ouvre une nouvelle fenêtre avec des informations d'aide.
        """
        self.fenetre_aide = QWidget()
        self.fenetre_aide.setWindowTitle("Aide")
        grid_aide = QGridLayout()
        self.fenetre_aide.setLayout(grid_aide)

        aide_lab = QLabel("Permet de convertir une température dans une unité vers une autre (C/K/F).")

        grid_aide.addWidget(aide_lab, 0, 0, 1, 3)

        self.fenetre_aide.show()
