# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowgvbPxz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QSlider, QToolButton, QVBoxLayout,
    QWidget)
from Resources import Resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setStyleSheet(u"QMainWindow{\n"
"   background-color:  #222831;\n"
"}\n"
"\n"
"QToolButton{\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton::pressed{\n"
" border: 1px solid #76ABAE; \n"
" border-radius: 17px;\n"
"}\n"
"\n"
"#video_progress::groove:horizontal{\n"
"      border: 1px solid #f7f7f7;\n"
"      height: 12px;\n"
"      background: #FFFBE6;\n"
"      margin: 2px 0;\n"
"}\n"
"\n"
"#video_progress::handle:horizontal{\n"
"       background: #1A3636;\n"
"       border: 1px solid #5c5c5c;\n"
"       width: 25px;\n"
"       border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0 , 0, 0)
        self.video_widget = QVideoWidget(self.centralwidget)
        self.video_widget.setObjectName(u"video_widget")

        self.verticalLayout.addWidget(self.video_widget)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_main_layout = QVBoxLayout()
        self.bottom_main_layout.setObjectName(u"bottom_main_layout")
        self.video_progress = QSlider(self.centralwidget)
        self.video_progress.setObjectName(u"video_progress")
        self.video_progress.setOrientation(Qt.Orientation.Horizontal)

        self.bottom_main_layout.addWidget(self.video_progress)

        self.bottom_main_layout_progress = QHBoxLayout()
        self.bottom_main_layout_progress.setObjectName(u"bottom_main_layout_progress")
        self.video_length_label = QLabel(self.centralwidget)
        self.video_length_label.setObjectName(u"video_length_label")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(18)
        self.video_length_label.setFont(font)

        self.bottom_main_layout_progress.addWidget(self.video_length_label)

        self.video_progress_label = QLabel(self.centralwidget)
        self.video_progress_label.setObjectName(u"video_progress_label")
        self.video_progress_label.setFont(font)
        self.video_progress_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.bottom_main_layout_progress.addWidget(self.video_progress_label)


        self.bottom_main_layout.addLayout(self.bottom_main_layout_progress)

        self.bottom_main_layout_controls = QHBoxLayout()
        self.bottom_main_layout_controls.setObjectName(u"bottom_main_layout_controls")
        self.backward_button = QToolButton(self.centralwidget)
        self.backward_button.setObjectName(u"backward_button")
        icon = QIcon()
        icon.addFile(u":/Icons/Previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backward_button.setIcon(icon)
        self.backward_button.setIconSize(QSize(35, 35))

        self.bottom_main_layout_controls.addWidget(self.backward_button)

        self.play_button = QToolButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(50, 50))

        self.bottom_main_layout_controls.addWidget(self.play_button)

        self.forward_button = QToolButton(self.centralwidget)
        self.forward_button.setObjectName(u"forward_button")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forward_button.setIcon(icon2)
        self.forward_button.setIconSize(QSize(35, 35))

        self.bottom_main_layout_controls.addWidget(self.forward_button)
        self.bottom_main_layout_controls.addStretch()

        self.mute_button = QToolButton(self.centralwidget)
        self.mute_button.setObjectName(u"mute_button")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Mute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mute_button.setIcon(icon3)
        self.mute_button.setIconSize(QSize(35, 35))

        self.bottom_main_layout_controls.addWidget(self.mute_button)

        self.volume_slider = QSlider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.bottom_main_layout_controls.addWidget(self.volume_slider)


        self.bottom_main_layout.addLayout(self.bottom_main_layout_controls)


        self.bottom_layout.addLayout(self.bottom_main_layout)


        self.verticalLayout.addLayout(self.bottom_layout)

        self.verticalLayout.setStretch(0, 80)
        self.verticalLayout.setStretch(1, 20)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Video Player", None))
#if QT_CONFIG(tooltip)
        self.video_widget.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Drag and drop a video file to play, or right click and load a video file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.video_length_label.setText(QCoreApplication.translate("mainWindow", u"00:00", None))
        self.video_progress_label.setText(QCoreApplication.translate("mainWindow", u"00:00", None))
        self.backward_button.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.play_button.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.forward_button.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.mute_button.setText(QCoreApplication.translate("mainWindow", u"...", None))
    # retranslateUi

