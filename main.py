from src.utils.utils import *
from kivy.app import App

class SommaApp(App):
    def calcola_somma(self, instance):
        try:
            # Ottieni il numero inserito dall'utente
            N1 = int(self.input_testo.text)
            
            # Calcola la somma dei numeri da 1 a N1
            somma1 = (N1 * (N1 + 1)) // 2
            self.etichetta.text = f"La somma dei numeri da 1 a {N1} è:\n{somma1}"
        
        except ValueError:
            self.etichetta.text = "Errore: Devi inserire un numero intero. Riprova."

# Esegui l'app
if __name__ == "__main__":
    SommaApp().run()