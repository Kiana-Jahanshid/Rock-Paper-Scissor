import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow ,  QMessageBox ,QLabel ,QFrame
from PySide6.QtUiTools import QUiLoader
from ui_rockpaperscissor import Ui_MainWindow 
from functools import partial
  
class RockPaperScissor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        
        self.rock = self.ui.rock_btn
        self.paper = self.ui.paper_btn
        self.scissor = self.ui.sci_btn
        self.win = self.ui.win_btn
        self.comp_score = self.ui.comp_score_btn
        self.player_score = self.ui.player_score_btn
        self.frame_player = self.ui.f1
        self.frame_comp = self.ui.f2
        self.comp_choice = ["✊🏻","✋🏻","✌🏻"]
        self.c_counter = 0
        self.p_counter = 0
        self.rock.clicked.connect(partial(self.play , "rock"))
        self.paper.clicked.connect(partial(self.play , "paper"))
        self.scissor.clicked.connect(partial(self.play , "scissor"))



    def play(self , input):
        global state_result
        state_result = input

        if state_result == "rock" :
            self.frame_player.setText("✊🏻")
        elif state_result == "paper" :
            self.frame_player.setText("✋🏻")
        elif state_result == "scissor":
            self.frame_player.setText("✌🏻")

        comp_result = self.comp_choice[random.randint(0,2)]
        self.frame_comp.setText(comp_result)


        if (state_result == "rock" and comp_result == self.comp_choice[2] ) or ( state_result == "paper" and comp_result == self.comp_choice[0] )  or (state_result == "scissor" and comp_result == self.comp_choice[1]):
            self.p_counter += 1 
            self.player_score.setText("Player Score :" + str(self.p_counter))

        elif (state_result == "scissor" and comp_result == self.comp_choice[0]) or (state_result == "rock" and comp_result == self.comp_choice[1]) or (state_result == "paper" and comp_result == self.comp_choice[2]):
            self.c_counter +=1 
            self.comp_score.setText("Computer Score :" +str(self.c_counter))


        if self.p_counter== 10  :
            self.win.setText("🎇🎈🎇🎈🎇 Player(YOU) Won 🎇🎈🎇🎈🎇")
        elif self.c_counter == 10 :
            self.win.setText("😛😛 Computer Won 😛😛")



app = QApplication(sys.argv)
main_window = RockPaperScissor()  
main_window.show()


app.exec()



