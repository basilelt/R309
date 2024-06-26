def divEntier(x:int, y:int) -> int:
    """
    Effectue une division entière.

    Cette fonction prend deux entiers, x et y, et effectue une division entière de x par y.

    Args:
        x (int): Le dividende.
        y (int): Le diviseur.

    Returns:
        int: Le résultat de la division entière de x par y.

    Raises:
        ZeroDivisionError: Si y est égal à zéro.
        ValueError: Si x ou y sont négatifs.
    """
    
    if y == 0:
        raise ZeroDivisionError("Le diviseur ne peut pas être égal à zéro.")
    
    if y < 0 or x < 0:
        raise ValueError("Le diviseur ou dénominateur ne peuvent pas être négatifs.")
    
    if x < y:
        return 0
    else:
        x = x - y

    return divEntier(x, y) + 1