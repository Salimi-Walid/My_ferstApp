from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.properties import DictProperty
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
import subprocess

# Set the initial window size
Window.size = (400, 600)

# KivyMD KV language string
KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: app.theme_cls.primary_color
    text_color: app.theme_cls.text_color
    icon_color: app.theme_cls.text_color
    ripple_color: app.theme_cls.accent_color
    selected_color: app.theme_cls.primary_color

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: app.theme_cls.text_color
    icon_color: app.theme_cls.text_color
    focus_behavior: False
    selected_color: app.theme_cls.text_color
    _no_ripple_effect: True

MDScreen:

    MDBottomNavigation:
        panel_color:"#027efa"
        MDBottomNavigationItem:
            name:'screen 1'
            text:"lessons"
            icon:"book-search"
            md_bg_color: "#f5f6f7"
            MDGridLayout:
                cols: 2
                spacing: "10dp"
                padding: "10dp"
                pos_hint: {"center_x": 0.6, "center_y": 0.3}
# les carde dyal les cours
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message("Card Clicked")
                    Image:
                        source: "image photochop\$.png"

                    MDLabel:
                        text: "2ème BAC"
                        

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message2("Card Clicked")
                    Image:
                        source: "your_image_path2.png"

                    MDLabel:
                        text: "1ère BAC"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message3("Card Clicked")

                    Image:
                        source: "your_image_path3.png"

                    MDLabel:
                        text: "Tronc Commun"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message4("Card Clicked")

                    Image:
                        source: "your_image_path4.png"

                    MDLabel:
                        text: "3ème année collège"
# la fin dyal card cours

# dowara dyal ajoutes cours
            MDFloatingActionButtonSpeedDial:
                id: speed_dial
                data: app.data
                root_button_anim: True
                hint_animation: True


        MDBottomNavigationItem:
            name:'screen 2'
            text: "Exercises"
            icon: "clipboard-text-outline"
            md_bg_color: "#f5f6f7"
# les card dyal exercice
            MDGridLayout:
                cols: 2
                spacing: "10dp"
                padding: "10dp"
                pos_hint: {"center_x": 0.6, "center_y": 0.3}
                
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message5("Card Clicked")
                    Image:
                        source: "your_image_path1.png"
                    
                    MDLabel:
                        text: "2ème BAC"
                        
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message6("Card Clicked")
                    Image:
                        source: "your_image_path2.png"
                    
                    MDLabel:
                        text: "1ère BAC"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message7("Card Clicked")
                    Image:
                        source: "your_image_path3.png"
                    
                    MDLabel:
                        text: "Tronc Commun"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message8("Card Clicked")
                    Image:
                        source: "your_image_path4.png"
                    
                    MDLabel:
                        text: "3ème année collège"
# la fin dyal card exercice
                    

        MDBottomNavigationItem:
            name: 'screen 3'
            text: "Exams"
            icon: "clipboard-text-multiple-outline"
            md_bg_color: "#f5f6f7"
# les card dyal exame
            MDGridLayout:
                cols: 2
                spacing: "10dp"
                padding: "10dp"
                pos_hint: {"center_x": 0.6, "center_y": 0.3}
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message9("Card Clicked")
                    Image:
                        source: "your_image_path1.png"
                    
                    MDLabel:
                        text: "2ème BAC"
                        
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message10("Card Clicked")
                    Image:
                        source: "your_image_path2.png"
                    
                    MDLabel:
                        text: "1ère BAC"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message11("Card Clicked")
                    Image:
                        source: "your_image_path3.png"
                    
                    MDLabel:
                        text: "Tronc Commun"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message12("Card Clicked")
                    Image:
                        source: "your_image_path4.png"
                    
                    MDLabel:
                        text: "3ème année collège"
# la fin card exame
# dowara dyal ajoutes cours
            MDFloatingActionButtonSpeedDial:
                id: speed_dial
                data: app.data
                root_button_anim: True
                hint_animation: True

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Najeh"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#027efa"
                    specific_text_color: "#f5f6f7"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["magnify", lambda x: app.on_search_icon_press(x),"sherch"]]


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "NAJEH"
                    source: ""
                    title_color: "black"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "account"
                    text_right_color: "#4a4939"
                    text: "Me"

                DrawerClickableItem:
                    icon: "account-hard-hat-outline"
                    text: "Support"

                DrawerClickableItem:
                    icon: "account-group"
                    text: "Discord community"

                DrawerClickableItem:
                    icon: "transcribe"
                    text: "Feedback"
                    on_release: app.show_feedback_confirmation_dialog()

                DrawerClickableItem:
                    icon: "exit-run"
                    text: "Exite"
                    on_release: app.show_exit_confirmation_dialog()

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"


'''


class Example(MDApp):
    data = DictProperty()

    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"

        self.data = {

            ' Add Exams': [
                'clipboard-text-multiple-outline',
                "on_press", lambda x: print("pressed JS"),
                "on_release", lambda x: print(
                    "stack_buttons",
                    self.root.ids.speed_dial.stack_buttons
                )
            ],
            'Add Exercice': [
                'clipboard-text-outline',
                "on_press", lambda x: print("pressed PHP"),
                "on_release", self.callback
            ],
            'Add Lessons': [
                'book-search',
                "on_press", lambda x: print("pressed C++"),
                "on_release", lambda x: self.callback()
            ],
        }

        return Builder.load_string(KV)




    def callback(self, *args):
        print(args)
# hadi dyal botton dya serching
    def on_search_icon_press(self, instance):
        print('Search icon pressed.')
        subprocess.Popen(["python", "serching.py"])

# hadi dyal exit
    def show_exit_confirmation_dialog(self):
        dialog = MDDialog(
            title="Exit Confirmation",
            text="Are you sure you want to exit?",
            buttons=[
                MDRaisedButton(text="Cancel", on_release=lambda x: dialog.dismiss()),
                MDRaisedButton(text="Exit", on_release=lambda x: self.stop())
            ]
        )
        dialog.open()
#hadi dyal fedback

    def show_feedback_confirmation_dialog(self):
        print("jj")

# mli katbrek 3la card :
    # les cours
    def show_message(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "sho3ba2bac.py"])
    def show_message2(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "sho3ba1bac.py"])
    def show_message3(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "sho3baTR.py"])
    def show_message4(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "sho3ba3.py"])
    # les exercice
    def show_message5(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message6(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message7(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message8(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    # les exams
    def show_message9(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message10(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message11(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])
    def show_message12(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "serching.py"])


Example().run()