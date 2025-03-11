# Questo modulo contiene la funzione calcola_somma che calcola la somma dei numeri interi
# da 1 fino a un numero dato. La funzione prende in input una stringa,
# tenta di convertirla in un intero, e se la conversione ha successo, calcola la somma dei numeri da 1 a quel numero
# utilizzando la formula della somma aritmetica. In caso di errore (ad esempio, se l'input non è un numero valido),
# la funzione restituisce None.

def calcola_somma(n1):
    """Calcola la somma dei numeri da 1 a n1."""
    try:
        n1:int = int(n1)
        return (n1 * (n1 + 1)) // 2
    except ValueError:
        return None  # Restituisce None in caso di errore