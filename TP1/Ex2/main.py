"""
Ce script lit un fichier texte et imprime son contenu.

Il accepte un argument de ligne de commande, -f, qui représente le chemin du fichier à lire.
Le script ouvre ensuite le fichier, lit toutes les lignes et les imprime.

Utilisation :
    python main.py -f <path_fichier>

Arguments:
    -f <path_fichier> (str): Le chemin du fichier à lire.

Lève :
    ValueError: Si aucun chemin de fichier n'est fourni.
    getopt.GetoptError: Si l'argument de ligne de commande n'est pas fourni dans le bon format.
    FileNotFoundError: Si le fichier n'existe pas.
    IOError: Si le fichier ne peut pas être ouvert.
    PermissionError: Si l'utilisateur n'a pas la permission d'ouvrir le fichier.
    IndexError: Si le chemin du fichier n'a pas été fourni.
"""

import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:", ["f="])
        if not args:
            raise ValueError("main.py -f <path_fichier>")
        path = args[0]
    except getopt.GetoptError:
        print("main.py -f <path_fichier>")
        sys.exit(2)
    
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    except IOError:
        print("Le fichier n'a pas pu être ouvert.")
    except PermissionError:
        print("Vous n'avez pas la permission d'ouvrir ce fichier")
    except IndexError:
        print("Le chemin du fichier n'a pas été fourni.")
    else:
        with open(path, "r") as f:
            lines = f.readlines()
            for l in lines:
                print(l.rstrip("\n\r"))
        # f.close() Pas nécessaire avec le with
    finally:
        print("Fin du programme")