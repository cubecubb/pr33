from kivy.config import Config
Config.set('graphics','resizable', False)

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label



class MyApp(App):
    
    def build(self):

        self.LabelFF = Label(text = "Код цвета")
        self.Label = Label(text = "Название цвета")

        bl = BoxLayout(orientation = 'vertical', spacing = 5)
        
        Window.size = (360, 700) 

        bl.add_widget(self.Label)

        bl.add_widget(self.LabelFF)


        # Красный
        bl.add_widget(Button(text ="#FF0000",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [1, 0, 0, 1],
        background_normal = ''))

        # Оранжевый
        bl.add_widget(Button(text ="#FF5500",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [255/255.0, 128/255.0, 0, 1],
        background_normal = ''))

        # Желтый
        bl.add_widget(Button(text ="#FFFF00",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [1, 1, 0, 1],
        background_normal = ''))
        
        # Зеленый
        bl.add_widget(Button(text ="#00FF00",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [0, 1, 0, 1],
        background_normal = ''))

        # Голубой
        bl.add_widget(Button(text ="#00FFFF",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [0, 1, 1, 1],
        background_normal = ''))

        # Синий
        bl.add_widget(Button(text ="#0000FF",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [0, 0, 255, 1],
        background_normal = ''))

        # Фиолетовый
        bl.add_widget(Button(text ="#FF00FF",
        font_size = "15sp",
        on_press = self.LabelFF_Code,
        background_color = [1, 0, 1, 1],))

        return bl
    

    def LabelFF_Code(self, instance):

        self.Label_Code = str(instance.text)

        if self.Label_Code == "#FF0000":
            self.Lable_text = 'Красный'
        if self.Label_Code == "#FF5500":
            self.Lable_text = 'Оранжевый'
        if self.Label_Code == "#FFFF00":
            self.Lable_text = 'Жёлтый'
        if self.Label_Code == "#00FF00":
            self.Lable_text = 'Зелёный'
        if self.Label_Code == "#00FFFF":
            self.Lable_text = 'Голубой'
        if self.Label_Code == "#0000FF":
            self.Lable_text = 'Синий'
        if self.Label_Code == "#FF00FF":
            self.Lable_text = 'Фиолетовый'

        self.update_LabelFF()

    def update_LabelFF(self):
        self.LabelFF.text = self.Label_Code    
        self.Label.text = self.Lable_text

if __name__ == "__main__":
    MyApp().run()
