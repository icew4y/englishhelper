# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLineEdit,
    QListView, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        if not MainDialog.objectName():
            MainDialog.setObjectName(u"MainDialog")
        MainDialog.resize(877, 561)
        self.gridLayout = QGridLayout(MainDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(MainDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.listView = QListView(MainDialog)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MainDialog)

        QMetaObject.connectSlotsByName(MainDialog)
    # setupUi

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QCoreApplication.translate("MainDialog", u"Dialog", None))
    # retranslateUi

