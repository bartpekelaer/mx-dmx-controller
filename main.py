from src.gui import MainWindow

import sys
from PySide6 import QtWidgets


def main() -> None:
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()