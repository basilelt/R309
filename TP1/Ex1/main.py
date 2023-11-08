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
    ValueError: Si aucun dividende ou diviseur n'est fourni.
    ValueError: Si les arguments fournis ne sont pas des entiers.
    ValueError: Si les arguments fournis ne sont pas des entiers positifs.
    getopt.GetoptError: Si les arguments de ligne de commande ne sont pas fournis dans le bon format.
    ZeroDivisionError: Si le diviseur est égal à zéro.
"""

from functions.div_entier import divEntier
import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "x:y:", ["x=", "y="])
        if not args or len(args) != 2:
            raise ValueError()
    except ValueError:
        print("main.py -x <dividende> -y <diviseur>")
        sys.exit(2)
    except getopt.GetoptError:
        print("main.py -x <dividende> -y <diviseur>")
        sys.exit(2)

    try:
        x = float(args[0])
        y = float(args[1])
        if x.is_integer() and y.is_integer():
            x = int(x)
            y = int(y)
        else:
            raise ValueError
    except ValueError:
        print("Les arguments doivent être des entiers")
        sys.exit(2)

    else:
        flag = False
        while not flag:
            try:
                print(divEntier(x, y))
            except ZeroDivisionError as err:
                print(err)
                y = int(input("y= "))
            except ValueError as err:
                try:
                    x = float(input("x= "))
                    y = float(input("y= "))
                    if x.is_integer() and y.is_integer():
                        x = int(x)
                        y = int(y)
                    else:
                        raise ValueError
                except ValueError:
                    print("Les arguments doivent être des entiers")
            else:
                flag = True
            