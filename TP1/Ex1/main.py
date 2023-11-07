"""
Ce script effectue une division entière.

Il accepte deux arguments de ligne de commande, -x et -y, qui représentent respectivement le dividende et le diviseur.
Le script effectue ensuite une division entière du dividende par le diviseur et imprime le résultat.

Utilisation :
    python main.py -x <dividende> -y <diviseur>

Arguments:
    -x <dividende> (int): Le nombre à diviser.
    -y <diviseur> (int): Le nombre par lequel diviser.

Lève :
    ValueError: Si les arguments fournis ne sont pas des entiers.
    getopt.GetoptError: Si les arguments de ligne de commande ne sont pas fournis dans le bon format.
"""

from functions.div_entier import divEntier
import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "x:y:", ["x=", "y="])
    except getopt.GetoptError:
        print("main.py -x <dividende> -y <diviseur>")
        sys.exit(2)

    try:
        int(args[0])
        int(args[1])
    except ValueError:
        print("Les arguments doivent être des entiers")
    else:
        print(divEntier(args[0], args[1]))
        