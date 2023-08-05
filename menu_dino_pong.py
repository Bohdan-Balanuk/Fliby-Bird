from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
# from dino_pong_game import*

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Меню")
main_window.resize(600, 200)

main_layout = QVBoxLayout()
layout1 = QVBoxLayout()
welcom_label = QLabel("Dino-Pong")
choose_label = QLabel("Виберіть рівень складності:")

button_easy = QPushButton("Легкий")
button_middle = QPushButton("Середный")
button_hard = QPushButton("Складний")

layout1.addWidget(welcom_label, alignment= Qt.AlignCenter)
layout1.addWidget(choose_label, alignment= Qt.AlignCenter)
layout1.addWidget(button_easy)
layout1.addWidget(button_middle)
layout1.addWidget(button_hard)

main_layout.addLayout(layout1) 

def choose_button_easy():
    global choose
    choose = 1
    main_window.close()

def choose_button_middle():
    global choose
    choose = 2
    main_window.close()

def choose_button_hard():
    global choose
    choose = 3
    main_window.close()

button_easy.clicked.connect(choose_button_easy)
button_middle.clicked.connect(choose_button_middle)
button_hard.clicked.connect(choose_button_hard)


main_window.setLayout(main_layout)
main_window.show()
app.exec_()
