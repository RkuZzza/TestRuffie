from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from ruffier import *
from instructions import *
from seconds import Seconds
from kivy.uix.image import Image

name = ""
age = 0
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        img = Image(source='pic.png')
        lb_name = Label(text="Введите имя:", halign="right")
        self.input_name = TextInput(multiline = False)
        lb_age = Label(text="Введите возраст:", halign="right")
        self.input_age = TextInput(text="7", multiline = False)
        self.btn = Button(text="Начать тест", size_hint=(0.3,0.1), pos_hint={"center_x":0.5})
        
        line1 = BoxLayout(size_hint=(0.8,None),height="30sp")
        line2 = BoxLayout(size_hint=(0.8,None),height="30sp")
        line1.add_widget(lb_name)
        line1.add_widget(self.input_name)
        line2.add_widget(lb_age)
        line2.add_widget(self.input_age)
        m_line = BoxLayout(orientation="vertical", padding=8, spacing = 8)
        m_line.add_widget(instr)
        m_line.add_widget(line1)
        m_line.add_widget(line2)
        m_line.add_widget(self.btn)
        self.add_widget(img)
        self.add_widget(m_line)
        self.btn.on_press = self.next
    def next(self):
        global name, age
        name = self.input_name.text
        age = check_int(self.input_age.text)
        if age == False or age < 7:
            age = 7
            self.input_age.text = str(age)
        else:
            self.manager.current = "pulse1"

class PulseScr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        instr = Label(text=txt_test1)
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.sec_finished)

        lb_result = Label(text="Введите результат:", halign="right")
        self.input_result = TextInput(text="0",multiline=False)
        self.input_result.set_disabled(True)
        self.btn = Button(text="Начать", size_hint=(0.3,0.1), pos_hint={"center_x":0.5})
        
        line = BoxLayout(size_hint=(0.8,None), height="30sp")
        line.add_widget(lb_result)
        line.add_widget(self.input_result)
        m_line = BoxLayout(orientation="vertical", spacing = 8, padding=8)
        m_line.add_widget(instr)
        m_line.add_widget(self.lbl_sec)
        m_line.add_widget(line)
        m_line.add_widget(self.btn)
        self.add_widget(m_line)
        self.btn.on_press = self.next
    
    def sec_finished(self, *args):
        self.next_screen = True
        self.input_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продолжить"
    
    def next(self):       
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.input_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.input_result.text = str(p1)
            else:
                self.manager.current = "sits"         

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text="Продолжить", size_hint=(0.3,0.1), pos_hint={"center_x":0.5})
        m_line = BoxLayout(orientation="vertical",  spacing = 8, padding=8)
        m_line.add_widget(instr)
        m_line.add_widget(self.btn)
        self.add_widget(m_line)
        self.btn.on_press = self.next
    def next(self):
        self.manager.current = "pulse2"

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0

        instr = Label(text=txt_test3)

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text="Считайте пульс")

        lb_result1 = Label(text="Результат:", halign="right")
        self.input_result1 = TextInput(text="0",multiline=False)
        h_line_1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        h_line_1.add_widget(lb_result1)
        h_line_1.add_widget(self.input_result1)

        lb_result2 = Label(text="Результат после отдыха:", halign="right")
        self.input_result2 = TextInput(text="0",multiline=False)
        h_line_2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        h_line_2.add_widget(lb_result2)
        h_line_2.add_widget(self.input_result2)

        self.input_result1.set_disabled(True)
        self.input_result2.set_disabled(True)

        self.btn = Button(text="Начать", size_hint=(0.3,0.1), pos_hint={"center_x":0.5})
        m_line = BoxLayout(orientation="vertical", spacing = 8, padding=8)
        m_line.add_widget(instr)
        m_line.add_widget(self.lbl1)
        m_line.add_widget(self.lbl_sec)
        m_line.add_widget(h_line_1)
        m_line.add_widget(h_line_2)
        m_line.add_widget(self.btn)
        self.add_widget(m_line)
        self.btn.on_press = self.next

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = "Отдыхайте"
                self.lbl_sec.restart(30)
                self.input_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text = "Считайте пульс"
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.input_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = "Завершить"
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.input_result1.text)
            p3 = check_int(self.input_result2.text)
            if p2 == False:
                p2 = 0
                self.input_result1 = str(p2)
            elif p3 == False:
                p3 = 0 
                self.input_result2 = str(p3)
            else:
                self.manager.current = "result"

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.m_line = BoxLayout(orientation = "vertical", spacing = 8, padding=8)
        self.instr = Label(text="")
        self.m_line.add_widget(self.instr)
        self.add_widget(self.m_line)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(p1,p2,p3,age)

class Heart(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name="instr"))
        sm.add_widget(PulseScr1(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        sm.current = "instr"
        return sm

app = Heart()
app.run()

