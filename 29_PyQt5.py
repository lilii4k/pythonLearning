import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI!")
        self.setGeometry(900, 500, 500, 300)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(10, 10, 70, 30)
        label.setStyleSheet("color: pink;"
                            "background-color: grey")

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("orangutan.jpg"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()