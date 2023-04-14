from pygame import*
from random import*
from time import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from dino_game import*
from dogonalki import*
from fliby_bird import*
from labirint_game import*



app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Меню")
main_window.resize(600, 200)

main_layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QVBoxLayout()
welcom = QLabel("Виберіть в яку гру ви хочите зіграти:")

button_first_game = QPushButton("Fliby Bird(1 player)")
button_second_game = QPushButton("Dino(1 player)")
button_third_game = QPushButton("Догонялки(2 players)")
button_fourth_game = QPushButton("Лабіринт(1 player)")
button_five_game = QPushButton("Dino-Pong (2 players)")

layout1.addWidget(button_first_game)
layout1.addWidget(button_second_game)
layout2.addWidget(button_third_game)
layout2.addWidget(button_fourth_game)
layout3.addWidget(welcom, alignment= Qt.AlignCenter)

layout3.addLayout(layout1)
layout3.addLayout(layout2)

main_layout.addLayout(layout3)
main_layout.addWidget(button_five_game)

def open_first_game():
    qm = QMessageBox()
    ok = qm.question(qm, "deket?", "Ви точно хочете цю гру?", qm.Yes | qm.No)
    if ok == qm.Yes:
        Fliby_bird_game()
        main_window.close()


def open_second_game():
    qm = QMessageBox()
    ok = qm.question(qm, "deket?", "Ви точно хочете цю гру?", qm.Yes | qm.No)
    if ok == qm.Yes:
        Dino_game()
        main_window.close()


def open_third_game():
    qm = QMessageBox()
    ok = qm.question(qm, "deket?", "Ви точно хочете цю гру?", qm.Yes | qm.No)
    if ok == qm.Yes:
        Dogonalki_game()
        main_window.close()


def open_fourth_game():
    qm = QMessageBox()
    ok = qm.question(qm, "deket?", "Ви точно хочете цю гру?", qm.Yes | qm.No)
    if ok == qm.Yes:
        Labirint_game()
        main_window.close()


def open_five_game():
    qm = QMessageBox()
    ok = qm.question(qm, "deket?", "Ви точно хочете цю гру?", qm.Yes | qm.No)
    if ok == qm.Yes:
        main_window.close()
        import dino_pong_game
        
        
button_first_game.clicked.connect(open_first_game)
button_second_game.clicked.connect(open_second_game)
button_third_game.clicked.connect(open_third_game)
button_fourth_game.clicked.connect(open_fourth_game)
if button_five_game.clicked.connect(open_five_game):
    ending = 1

main_window.setLayout(main_layout)
main_window.show()
app.exec_()