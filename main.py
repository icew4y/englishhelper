import sys
import traceback

import PySide6
import urllib3
from PySide6 import QtCore
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from maindialog import MainDialog

if __name__ == '__main__':
    log_file = "logs.txt"
    try:
        QtCore.QCoreApplication.setAttribute(PySide6.QtCore.Qt.ApplicationAttribute.AA_UseOpenGLES)
        app = QApplication(sys.argv)
        maindialog = MainDialog()
        rc = maindialog.exec()
    except Exception as e:
        with open(log_file, 'a+', encoding="utf-8") as f:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=10, file=f)
            QMessageBox.critical(None, "错误", repr(traceback.format_exception(exc_type, exc_value,
                                                                             exc_traceback)), QMessageBox.StandardButton.Ok)