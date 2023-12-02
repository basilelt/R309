from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QGridLayout, QComboBox
import time, threading, socket

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        widget = QWidget ()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Compteur :")
        self.__compteur_value = 0
        self.__compteur = QLineEdit(f"{self.__compteur_value}")
        self.__compteur.setReadOnly(True)

        start = QPushButton("Start")
        reset = QPushButton("Reset")
        stop = QPushButton("stop")
        connect = QPushButton("Connect")
        quitter = QPushButton("Quitter")

        grid.addWidget(lab, 0, 0, 1, 1)
        grid.addWidget(self.__compteur, 1, 0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 0, 1, 1)
        grid.addWidget(stop, 3, 1, 1, 1)
        grid.addWidget(connect, 4, 0, 1, 1)
        grid.addWidget(quitter, 4, 1, 1, 1)

        self.setWindowTitle("Chronomètre")

        self.__status = False
        self.__status2 = False
        self.__client_socket_tcp = None
        self.__sock = False

        self.__test_addition = 0
        self.__test = 0

        start.clicked.connect(self.start)
        reset.clicked.connect(self.__reset)
        quitter.clicked.connect(self.__close)
        stop.clicked.connect(self.__stop)
        connect.clicked.connect(self.__connect)


    def start(self):
        if self.__sock:
            try:
                self.__client_socket_tcp.send(("Start").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False

        self.__arret_thread = False

        thread = threading.Thread(target=self.__start)
        thread.start()

        self.__status = True


    def __start(self):
        if self.__sock:
            try:
                self.__client_socket_tcp.send((f"{self.__compteur_value}").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False

        while self.__arret_thread == False:
            time.sleep(1)
            if self.__arret_thread == True:
                break

            self.__compteur_value += 1
            
            ## Partie vérification si addition texte
            try:
                self.__test_addition = float(self.__compteur_value + self.__test)
                print(self.__test_addition)
            except:
                print("Erreur de type")
            ## Fin de la partie

            self.__compteur.setText(f"{self.__compteur_value}")

            if self.__sock:
                try:
                    self.__client_socket_tcp.send((f"{self.__compteur_value}").encode())
                except(ConnectionResetError):
                    print("Connexion réinitialisée")
                    self.__sock = False
                except(BrokenPipeError):
                    print("Rupture de la connexion")
                    self.__sock = False

        self.__status = False
        self.__status2 = False


    def __reset(self):
        if self.__sock:
            try:
                self.__client_socket_tcp.send(("Reset").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False
        
        ## Ne pas appeler __stop car is connecter au serveur, il va envoyer un "stop" au serveur
        self.__arret_thread = True
        while self.__status == True or self.__status2 == True:
            time.sleep(0.1)

        self.__compteur_value = 0
        self.__compteur.setText(f"{self.__compteur_value}")


    def __close(self):
        if self.__sock:
            try:
                self.__client_socket_tcp.send(("Quitter").encode())
                self.__client_socket_tcp.send(("bye").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False
            self.__sock = False

        self.__stop()
        QApplication.exit(0)

    
    def __stop(self):
        if self.__sock:
            try:
                self.__client_socket_tcp.send(("stop").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False

        self.__arret_thread = True
        while self.__status == True or self.__status2 == True:
            time.sleep(0.1)


    def __connect(self):
        if self.__sock == False:
            self.__status2 = True
            thread = threading.Thread(target=self.__thread_co)
            thread.start()
        else:
            try:
                self.__client_socket_tcp.send(("Connect").encode())
            except(ConnectionResetError):
                print("Connexion réinitialisée")
                self.__sock = False
            except(BrokenPipeError):
                print("Rupture de la connexion")
                self.__sock = False


    def __thread_co(self):
        try:
            self.__client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client_socket_tcp.connect(("localhost", 10000))
            self.__client_socket_tcp.send(("Connect").encode())
            
            self.__sock = True
            while self.__sock:
                maintainer = "Le socket est maintenu"
        
        except(socket.gaierror):
            print("Erreur lors de la résolution de l'hôte")
        
        except(ConnectionRefusedError):
            print("Connexion refusée")
        
        except(TimeoutError):
            print("Timeout")
        
        except(ConnectionResetError):
            print("Connexion réinitialisée")
        
        except(BrokenPipeError):
            print("Rupture de la connexion")
        
        finally:
            self.__sock = False
            self.__status2 = False
            self.__client_socket_tcp.close()

