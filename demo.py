import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QVBoxLayout, QSpinBox
import random

layout = QVBoxLayout()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(100,100, 400, 400)
        self.num_pass()
        self.length_pass()
        self.execute()
        self.initUI()
        self.show()

    def initUI(self):
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(QLabel('Welcome to Password Generator!',alignment=Qt.AlignCenter))
        self.vbox.addWidget(QLabel(f'Here are your {self.num_value} unique passwords:',alignment=Qt.AlignCenter))
        self.vbox.addWidget(QLabel(f'{self.passwords}', alignment=Qt.AlignCenter))

        self.setLayout(self.vbox)
        self.setGeometry(100,100, 400, 400)
        self.setWindowTitle('QLabel')
        self.show()

        
    def num_pass(self):
        self.num_value, okPressed = QInputDialog.getInt(self, "Password Amount:","Number:", 0, 1, 50, 1)
        if okPressed:
            print(self.num_value)


    def length_pass(self):
        self.len_value, okPressed = QInputDialog.getInt(self, "Password Length: ","Length:", 0, 1, 50, 1)
        if okPressed:
            print(self.len_value)

   
			
    def execute(self):
        char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_,./?'
        number = self.num_value
        length = self.len_value
        print(f'\nHere is {number} unique passwords: ')

        for password in range(self.num_value):
            self.passwords = ''
            for chars in range(self.len_value):
                self.passwords += random.choice(char)
            print(f'\t{self.passwords}')
        


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
