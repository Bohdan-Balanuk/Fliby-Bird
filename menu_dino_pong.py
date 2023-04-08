from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

print(1)
#менюшка

app = QApplication([])
main_wind = QWidget()
main_wind.setWindowTitle("Меню")
main_wind.resize(600, 200)

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

choose = 0 

def choose_button_easy():
    global choose
    choose = 1
    main_wind.close()

def choose_button_middle():
    global choose
    choose = 2
    main_wind.close()

def choose_button_hard():
    global choose
    choose = 3
    main_wind.close()

button_easy.clicked.connect(choose_button_easy)
button_middle.clicked.connect(choose_button_middle)
button_hard.clicked.connect(choose_button_hard)


main_wind.setLayout(main_layout)
main_wind.hide()
