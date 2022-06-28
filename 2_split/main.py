from os.path import dirname, join
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class UpArea(BoxLayout):
    pass


class DownArea(BoxLayout):
    pass


class MainApp(App):
    kv_file = 'sample.kv'
    
    def build(self):
        return Builder.load_file(join(dirname(__file__), self.kv_file))
    

def main():
    MainApp().run()


if __name__ == "__main__":
    main()