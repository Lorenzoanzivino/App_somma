# Importazione della classe SommaApp dal modulo `utils`, che contiene la logica dell'applicazione.
# L'app viene eseguita nel blocco principale, avviando l'interfaccia grafica.

from src.utils.utils import SommaApp  # Importa la classe corretta

# Esegui l'app
if __name__ == "__main__":
    SommaApp().run()