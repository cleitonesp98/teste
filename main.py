from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDIconButton,MDFloatingActionButton,MDRectangleFlatButton
from kivymd.uix.button import MDRaisedButton,MDRectangleFlatIconButton,MDFillRoundFlatIconButton

class testeApp(MDApp):
    Window.size=(300,600)
    def build(self):
        boxlayout = MDBoxLayout(
            orientation = 'vertical',
            pos_hint={'center_x':0.5,'center_y':0.7},
            spacing = 15
        )

        btn1 =MDFlatButton(
            text = 'login',
            pos_hint={'center_x':0.5,'center_y':0.5}, ##BOTAO COM TEXTO
        )
        btn2 =MDIconButton(
            icon='folder',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO COM ICONE NORMAL
        )
        btn3 =MDFloatingActionButton(
            icon='folder',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO SUSPENSO
        )
        btn4 =MDRectangleFlatButton(
            text = 'login',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO COM TEXTO DENTRO DE UM RETANGULO BRANCO COM BORDA
        )
        btn5 =MDRaisedButton(
            text = 'login',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO COM TEXTO DENTRO DE UM RETANGULO COLORIDO
        )
        
        btn6=MDRectangleFlatIconButton(
            text = 'login',
            icon='folder',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO COM TEXTO E ICONE DENTRO DE UM RETANGULO BRANCO COM BORDA

        )
        btn7=MDFillRoundFlatIconButton(
            text = 'login',
            icon='folder',
            pos_hint={'center_x':0.5,'center_y':0.5} ##BOTAO COM TEXTO E ICONE DENTRO DE UM RETANGULO BORDA BRANCO COM BORDA

        )
        label = MDLabel(
            text="Teste",
            halign="center",
            theme_text_color='Custom',
            text_color = (0,1,0,1)
            )
                        #texto      ,#alinhamento do texto , #habilitar edição te
        boxlayout.add_widget(btn1)
        boxlayout.add_widget(btn2)
        boxlayout.add_widget(btn3)
        boxlayout.add_widget(btn4)
        boxlayout.add_widget(btn5)
        boxlayout.add_widget(btn6)
        boxlayout.add_widget(btn7)
        #boxlayout.add_widget(label)
        return boxlayout

testeApp().run()