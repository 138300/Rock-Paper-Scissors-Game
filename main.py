from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from game_ui import Ui_GameWindow
import random,time

# region game window
class GameWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.game=Ui_GameWindow()
        self.game.setupUi(self)

        self.game.stackedWidget.setCurrentWidget(self.game.welcome_page)
        self.game.start_btn.clicked.connect(lambda:self.game.stackedWidget.setCurrentWidget(self.game.round_page))
        self.game.start_again_btn.clicked.connect(self.play_again)
        self.game.rounds_3_btn.clicked.connect(self.three_rounds)
        self.game.rounds_6_btn.clicked.connect(self.six_rounds)
        
        self.game.your_choice.setPixmap(QPixmap(''))
        self.game.computer_choice.setPixmap(QPixmap(''))

        self.game.y_rock_btn.clicked.connect(self.rock)
        self.game.y_paper_btn.clicked.connect(self.paper)
        self.game.y_scissors_btn.clicked.connect(self.scissors)

        self.show()

        # scores and round
        self.round=0
        self.your_score=0
        self.computer_score=0
        

    # region rounds functions
    def three_rounds(self):
        self.game.stackedWidget.setCurrentWidget(self.game.game_page)
        self.count_of_rounds=3 

    def six_rounds(self):
        self.game.stackedWidget.setCurrentWidget(self.game.game_page)
        self.count_of_rounds=6
    # endregion

    # region game functions
    def rock(self):
        self.round+=1
        self.game.your_choice.setPixmap(QPixmap(''))
        self.game.your_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/stone (2).png'))
        computer_choice=random.choice(['rock','paper','scissors'])
        
        if computer_choice=='rock':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/stone (2).png'))
            self.your_score+=0
            self.computer_score+=0
          
        elif computer_choice=='paper':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/paper.png'))
            self.your_score+=0
            self.computer_score+=1

        elif computer_choice=='scissors':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/scissors.png'))
            self.your_score+=1
            self.computer_score+=0

        self.game.y_score.setText('Your Score:%s'%(self.your_score))
        self.game.c_score.setText('Computer Score:%s'%(self.computer_score))
        self.game.round_lbl.setText('Round:%s'%(self.round))
        
     
        if self.count_of_rounds+1==self.round+1:
            self.game.stackedWidget.setCurrentWidget(self.game.finished_page)
                
            if self.your_score>self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/king.png'))
                self.game.title_2.setStyleSheet('color:#FF9A00')
                self.game.title_2.setText('You Won\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score<self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/game-over.png'))
                self.game.title_2.setStyleSheet('color:#FF2E63')
                self.game.title_2.setText('You Lost\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score==self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setStyleSheet('color:#3FC1C9')
                self.game.title_2.setText('Tie\n%s:%s'%(self.your_score,self.computer_score))


    def paper(self):
        self.round+=1
        self.game.your_choice.setPixmap(QPixmap(''))
        self.game.your_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/paper.png'))
        computer_choice=random.choice(['rock','paper','scissors'])
        
        if computer_choice=='rock':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/stone (2).png'))
            self.your_score+=1
            self.computer_score+=0
          
        elif computer_choice=='paper':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/paper.png'))
            self.your_score+=0
            self.computer_score+=0

        elif computer_choice=='scissors':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/scissors.png'))
            self.your_score+=0
            self.computer_score+=1

        self.game.y_score.setText('Your Score:%s'%(self.your_score))
        self.game.c_score.setText('Computer Score:%s'%(self.computer_score))
        self.game.round_lbl.setText('Round:%s'%(self.round))

        if self.count_of_rounds==self.round:
            self.game.stackedWidget.setCurrentWidget(self.game.finished_page)
                
            if self.your_score>self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/king.png'))
                self.game.title_2.setStyleSheet('color:#FF9A00')
                self.game.title_2.setText('You Won\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score<self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/game-over.png'))
                self.game.title_2.setStyleSheet('color:#FF2E63')
                self.game.title_2.setText('You Lost\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score==self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setStyleSheet('color:#3FC1C9')
                self.game.title_2.setText('Tie\n%s:%s'%(self.your_score,self.computer_score))


    def scissors(self):
        self.round+=1
        self.game.your_choice.setPixmap(QPixmap(''))
        self.game.your_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/scissors.png'))
        computer_choice=random.choice(['rock','paper','scissors'])
        
        if computer_choice=='rock':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/stone (2).png'))
            self.your_score+=0
            self.computer_score+=1
          
        elif computer_choice=='paper':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/paper.png'))
            self.your_score+=1
            self.computer_score+=0

        elif computer_choice=='scissors':
            self.game.computer_choice.setPixmap(QPixmap(''))
            self.game.computer_choice.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/scissors.png'))
            self.your_score+=0
            self.computer_score+=0

        self.game.y_score.setText('Your Score:%s'%(self.your_score))
        self.game.c_score.setText('Computer Score:%s'%(self.computer_score))
        self.game.round_lbl.setText('Round:%s'%(self.round))


        if self.count_of_rounds==self.round:
            self.game.stackedWidget.setCurrentWidget(self.game.finished_page)
                
            if self.your_score>self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.title_2.setStyleSheet('color:#FF9A00')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/king.png'))
                self.game.title_2.setText('You Won\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score<self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap('../../../../../Users/M.ALI/Downloads/game-over.png'))
                self.game.title_2.setStyleSheet('color:#FF2E63')
                self.game.title_2.setText('You Lost\n%s:%s'%(self.your_score,self.computer_score))

            if self.your_score==self.computer_score:
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setText('')
                self.game.king_icon.setPixmap(QPixmap(''))
                self.game.title_2.setStyleSheet('color:#3FC1C9')
                self.game.title_2.setText('Tie\n%s:%s'%(self.your_score,self.computer_score))
   
    # endregion    
    
    def play_again(self):
        self.round=0
        self.your_score=0
        self.computer_score=0
        self.game.y_score.setText('Your Score:0')
        self.game.c_score.setText('Computer Score:0')
        self.game.round_lbl.setText('Round:0')
        self.game.your_choice.setPixmap(QPixmap(''))
        self.game.computer_choice.setPixmap(QPixmap(''))
        self.game.stackedWidget.setCurrentWidget(self.game.round_page)
# endregion



if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window=GameWindow()
    sys.exit(app.exec_())



