from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from decimal import Decimal


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        main_layout = RelativeLayout()
        frame1 = BoxLayout(
            orientation='vertical', spacing=0,
            size_hint=(None, None), size=(150, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        photo = Image(
            source='data/apk_logo.jpg',
            size_hint_y=None,
            height=120,
            # pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        label1 = Label(text='Golden Ratio Converter\nFor Fun Use\nDeveloped by\nAPK_Soft\n2024', size_hint_y=None, height=200,halign = 'center')
        button_back = Button(
            text='Back', 
            size_hint_y=None, 
            height=30,
            background_color=(1, 0.8, 0, 1),
            on_press=self.switch_to_main_screen,
            )
        frame1.add_widget(photo)
        frame1.add_widget(label1)
        frame1.add_widget(button_back)
        main_layout.add_widget(frame1)
        
        # Set main_layout as the root widget of the screen
        self.add_widget(main_layout)

    def switch_to_main_screen(self, instance):
        self.manager.current = 'main'


class FrameExample(App):
    input_value = NumericProperty(0)

    def build(self):
        # Screen Manager to manage multiple screens
        screen_manager = ScreenManager()

        # Main Screen
        main_screen = Screen(name='main')
        main_layout = RelativeLayout()

        # Add a background image
        background_image = Image(
            source='data/background.jpg',
            allow_stretch=True,
            keep_ratio=False,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        main_layout.add_widget(background_image)

        # Frame 1: Vertical BoxLayout
        frame1 = BoxLayout(
            orientation='vertical', spacing=5,
            size_hint=(None, None), size=(150, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )
        label1 = Label(text='Golden Ratio Converter', size_hint_y=None, height=50)
        photo = Image(
            source='data/Logo.jpg',
            size_hint_y=None,
            height=110,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        frame1.add_widget(photo)
        frame1.add_widget(label1)

        # Frame 2: GridLayout
        frame2 = BoxLayout(
            orientation='vertical', spacing=5,
            size_hint=(None, None), size=(150, 110),
            pos_hint={'center_x': 0.5, 'center_y': 0.65}
        )
        entry = TextInput(
            multiline=False,
            size_hint_y=None,
            height=30,
            size_hint_x=None,
            width=150,
            text="0.00",  # Set default text
            input_filter=lambda text, from_undo: text if text == "" or text.replace(".", "").isdigit() else "",
        )
        entry.text = '0.00'
        
        button2 = Button(
            text='Convert',
            size_hint_y=None,
            height=30,
            size_hint_x=None,
            width=150,
            background_color=(1, 0.8, 0, 1),
            on_press=lambda instance: self.on_button_press(entry)
        )
        frame2.add_widget(entry)
        frame2.add_widget(button2)

        # Frame 2 Result: Vertical BoxLayout
        frame2_result = BoxLayout(
            orientation='vertical', spacing=5,
            size_hint=(None, None), size=(150, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.44}
        )
        self.label_result = Label(
            text=f"Please enter a value",
            size_hint_y=None,
            height=30
        )
        frame2_result.add_widget(self.label_result)

        # Frame 3: Another Vertical BoxLayout
        frame3 = BoxLayout(
            orientation='vertical', spacing=5,
            size_hint=(None, None), size=(150, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.33}
        )
        button3 = Button(
            text='About',
            size_hint_y=None,
            height=21,
            size_hint_x=None,
            width=150,
            background_color=(0.7, 0.7, 0.7, 1),
            on_press=self.on_about_button_press
        )
        frame3.add_widget(button3)

        main_layout.add_widget(frame1)
        main_layout.add_widget(frame2)
        main_layout.add_widget(frame2_result)
        main_layout.add_widget(frame3)
        main_screen.add_widget(main_layout)

        # About Screen
        about_screen = AboutScreen(name='about')
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(about_screen)

        return screen_manager

    def on_button_press(self, entry):
        try:
            input_value = float(entry.text.replace(",", "."))
            self.input_value = input_value
            phi_value = (1 + Decimal(5).sqrt()) / Decimal(2)
            self.label_result.text = f'Golden Result:\n{Decimal(self.input_value) * phi_value}'
            self.label_result.halign = 'center'
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def on_about_button_press(self, instance):
        self.root.current = 'about'

if __name__ == '__main__':
    FrameExample().run()
