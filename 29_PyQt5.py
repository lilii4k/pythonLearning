import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI!")
        self.setGeometry(900, 500, 800, 600)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(10, 10, 70, 30)
        label.setStyleSheet("color: orange;"
                            "background-color: white")
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        image_label = QLabel(self)
        pixmap = QPixmap("orangutan.jpg")  # Load your image
        image_label.setPixmap(pixmap)
        image_label.setGeometry(30, 30, 500, 500)  # x, y, width, height
        image_label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("orangutan.jpg"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()