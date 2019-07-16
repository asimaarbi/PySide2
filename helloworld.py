import sys

from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World")

    # Displaying html in the label
    label = QLabel("<font color=red size=40>Hello World</font>")

    label.show()
    sys.exit(app.exec_())
