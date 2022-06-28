from os.path import dirname
from os.path import join
from secrets import SystemRandom

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

kv_file = 'lotto.kv'
Builder.load_file(join(dirname(__file__), kv_file))


class RootLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        self.lotto = Lotto()

    def button01_clicked(self):
        self.lbl_num01.text = self.lotto.get_number_1()
        self.lbl_num02.text = self.lotto.get_number_2()
        self.lbl_num03.text = self.lotto.get_number_3()
        self.lbl_num04.text = self.lotto.get_number_4()
        self.lbl_num05.text = self.lotto.get_number_5()
        self.lbl_num06.text = self.lotto.get_number_6()

    def button02_clicked(self):
        self.lotto = Lotto()
        self.lbl_num01.text = ''
        self.lbl_num02.text = ''
        self.lbl_num03.text = ''
        self.lbl_num04.text = ''
        self.lbl_num05.text = ''
        self.lbl_num06.text = ''


class MainApp(App):
    def build(self):
        return RootLayout()


class Lotto:
    def __init__(self):
        self.number_list = list(range(1, 45))
        self.lotto_num = SystemRandom().sample(self.number_list, 6)

    def get_number_1(self):
        return str(self.lotto_num[0])

    def get_number_2(self):
        return str(self.lotto_num[1])

    def get_number_3(self):
        return str(self.lotto_num[2])

    def get_number_4(self):
        return str(self.lotto_num[3])

    def get_number_5(self):
        return str(self.lotto_num[4])

    def get_number_6(self):
        return str(self.lotto_num[5])


def main():
    MainApp().run()


if __name__ == "__main__":
    main()