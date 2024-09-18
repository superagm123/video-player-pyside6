import sys 
import platform 
import time
from pathlib import Path
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMenu, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import Qt
from View.MainWindow import Ui_mainWindow
from Model.VideoPlayer import VideoPlayer


VIDEO_PATH = f"{Path.home()}{"/Movies" if platform.system() == "Darwin" else "\\Video"}"

class MainWindow(QMainWindow, Ui_mainWindow):
    is_muted = False
    is_progress_pressed = False
    previous_volume = 0
    duration = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.video_widget.setAcceptDrops(True)
        self.set_context_menu_policy()
        self.set_volume_slider()
        self.video_player = VideoPlayer(video_output=self.video_widget)
        self.set_signals_connection()

    #Drag & drop methods
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        event.setDropAction(Qt.CopyAction)
        video = event.mimeData().urls()[0].toLocalFile()
        self.video_player.set_video_source(video=video)
        event.accept()

    def set_volume_slider(self):
        self.volume_slider.setValue(50)
        self.volume_slider.setRange(0, 100)

    def set_context_menu_policy(self):
        self.video_widget.setContextMenuPolicy(Qt.CustomContextMenu)
    
    def set_signals_connection(self):
        self.video_widget.customContextMenuRequested.connect(self.show_context_menu)
        self.video_widget.mouseDoubleClickEvent = lambda _: self.load_video()
        self.video_player.signals.videoDurationChanged.connect(self.update_video_duration)
        self.video_player.signals.videoPositionChanged.connect(self.update_video_progress)
        self.video_player.signals.videoStateChanged.connect(self.toggle_play_button_icon)
        self.volume_slider.valueChanged.connect(self.update_audio_volume)
        self.video_progress.sliderPressed.connect(self.progress_pressed)
        self.video_progress.sliderReleased.connect(self.progress_released)
        self.backward_button.clicked.connect(self.play_backward)
        self.play_button.clicked.connect(self.play)
        self.forward_button.clicked.connect(self.play_forward)
        self.mute_button.clicked.connect(self.mute)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        menu.addAction("Load a video file", self.load_video)
        menu.exec(self.video_widget.mapToGlobal(pos))

    def toggle_play_button_icon(self):
        state = self.video_player.get_video_player_state()
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setIcon(QIcon("Resources/Pause.png"))
        else:
            self.play_button.setIcon(QIcon("Resources/Play.png"))

    def load_video(self):
        video = QFileDialog.getOpenFileName(self, "Open a video file", VIDEO_PATH, "All Files(*) *.mp4 *.m4v *.avi *.mov")[0]

        if video:
            self.video_player.set_video_source(video=video)

    def progress_pressed(self):
        self.is_progress_pressed = True

    def progress_released(self):
        self.is_progress_pressed = False
        self.video_player.set_video_position(self.video_progress.value() * 1000)

    def play_backward(self):
        self.video_player.set_video_position((self.video_progress.value() - 10) * 1000)

    def play(self):
        self.video_player.play()

    def play_forward(self):
        self.video_player.set_video_position((self.video_progress.value() + 10) * 1000)

    def mute(self):
        if self.is_muted:
            self.volume_slider.setValue(self.previous_volume)
        else:
            self.previous_volume = self.volume_slider.value()
            self.volume_slider.setValue(0)

    def update_audio_volume(self):
        volume = self.volume_slider.value() / 100
        self.video_player.set_audio_output_volume(volume)
        if volume == 0:
            self.mute_button.setIcon(QIcon("Resources/Unmute.png"))
            self.is_muted = True
        else:
            self.mute_button.setIcon(QIcon("Resources/Mute.png"))
            self.is_muted = False


    def update_video_duration(self, duration):
        self.duration = duration
        self.video_progress.setRange(0, duration)

    def update_video_progress(self, position):
        self.video_length_label.setText(time.strftime("%M:%S", time.gmtime(self.duration - position)))
        self.video_progress_label.setText(time.strftime("%M:%S", time.gmtime(position)))
        if not self.is_progress_pressed:
            self.video_progress.setValue(position)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()