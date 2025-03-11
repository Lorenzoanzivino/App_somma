
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

#class SommaApp(App):
def build(self):
    Window.clearcolor = (1, 1, 1, 1)  # bianco (R, G, B, A)
    self.window = GridLayout()
    self.window.cols = 1
    self.window.size_hint = (0.8, 0.9)
    self.window.pos_hint = {"center_x": 0.5, "center_y": 0.4}
    Window.size = (360, 640)
        
    self.window.add_widget(Image(source="image/soldi.png"))
        
    self.input_testo = TextInput(
        size_hint =(1, 0.2),
        font_size = '20sp',
        padding = (10, 12),
        halign = 'center'
            )
    self.window.add_widget(self.input_testo)
        
    self.bottone = Button(
        text="CALCOLA!",
        size_hint = (1, 0.2),
        bold = True,
        background_color = '#0099ff'
        )
    self.window.add_widget(self.bottone)
    self.bottone.bind(on_press = self.calcola_somma)
        
    self.etichetta = Label(
        text="Inserisci un numero intero...",
        font_size = '18sp',
        color = '#007dd1',
        halign ='center',
        valign='middle',
        )
    self.window.add_widget(self.etichetta)
        

    return self.window