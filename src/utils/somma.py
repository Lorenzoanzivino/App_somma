def calcola_somma(n1):
    """Calcola la somma dei numeri da 1 a n1."""
    try:
        n1:int = int(n1)
        return (n1 * (n1 + 1)) // 2
    except ValueError:
        return None  # Restituisce None in caso di errore