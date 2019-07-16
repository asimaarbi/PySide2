import random
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
                      "Hola Mundo", "Привет мир"]

        self.greeting = QPushButton("Greeting!")
        self.exit_butn = QPushButton('Exit')
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.greeting)
        self.layout.addWidget(self.exit_butn)
        self.setLayout(self.layout)

        self.greeting.clicked.connect(self.magic)
        self.exit_butn.clicked.connect(app.exit)

    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
