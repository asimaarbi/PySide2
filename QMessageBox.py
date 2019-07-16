import sys

from PySide2.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

msg_box = QMessageBox()
msg_box.setText(("Hello World!"))
msg_box.show()

sys.exit(msg_box.exec_())
