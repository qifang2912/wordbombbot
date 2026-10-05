import sys

from PySide6.QtWidgets import QApplication
from overlay import Overlay


app = QApplication(sys.argv)

window = Overlay()
window.show()

sys.exit(app.exec())