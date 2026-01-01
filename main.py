from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import google.generativeai as genai

# Ustawienie tła na czarne
Window.clearcolor = (0, 0, 0, 1)

class PaulaApp(App):
    def build(self):
        self.title = "Paula AI"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # --- KONFIGURACJA AI ---
        genai.configure(api_key="TWÓJ_KLUCZ_API_TUTAJ")
        self.model = genai.GenerativeModel('gemini-1.5-flash')

        self.label = Label(
            text="Cześć, jestem Paula!", 
            font_size='20sp',
            color=(0, 0.7, 1, 1),
            text_size=(Window.width - 40, None),
            halign='center'
        )
        
        self.input = TextInput(
            hint_text="Napisz do Pauli...", 
            multiline=False, 
            size_hint_y=None, 
            height=120,
            font_size='18sp'
        )
        
        self.btn = Button(
            text="ZAPYTAJ PAULE", 
            size_hint_y=None, 
            height=120, 
            background_color=(0, 0.4, 0.8, 1),
            font_size='20sp',
            bold=True
        )
        self.btn.bind(on_press=self.send_message)

        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(self.btn)
        return layout

    def send_message(self, instance):
        user_text = self.input.text
        if user_text:
            self.label.text = "Paula myśli..."
            try:
                response = self.model.generate_content(f"Jesteś Paula, odpisz krótko: {user_text}")
                self.label.text = response.text
                self.input.text = ""
            except Exception as e:
                self.label.text = "Błąd: Brak internetu lub zły klucz."

if __name__ == "__main__":
    PaulaApp().run()
