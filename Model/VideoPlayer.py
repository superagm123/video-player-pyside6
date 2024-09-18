from functools import partial
from PySide6.QtWidgets import QMessageBox, QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, Slot, QUrl, QTimer
from Model.Signals import VideoPlayerSignals 


class VideoPlayer(QWidget):
    def __init__(self, video_output: object):
        super().__init__()
        self.__audio_output = QAudioOutput()
        self.__video_player = QMediaPlayer()
        self.__video_output = video_output
        self.__video_player.setVideoOutput(self.__video_output)
        self.__setup_player()
        self.__set_player_signals_connection()
        self.signals = VideoPlayerSignals()

    def __setup_player(self):
        self.__audio_output.setVolume(50)
        self.__video_player.setAudioOutput(self.__audio_output)
        self.__video_output.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)

    def __set_player_signals_connection(self):
        self.__video_player.durationChanged.connect(self.__video_duration_changed)
        self.__video_player.positionChanged.connect(self.__video_position_changed)
        self.__video_player.mediaStatusChanged.connect(self.__video_status_changed)
        self.__video_player.playbackStateChanged.connect(self.__video_state_changed)

    @Slot()
    def __video_duration_changed(self, duration):
        self.signals.videoDurationChanged.emit(duration // 1000)

    @Slot()
    def __video_position_changed(self, position):
        self.signals.videoPositionChanged.emit(position // 1000)

    @Slot()
    def __video_state_changed(self, state):
        self.signals.videoStateChanged.emit(state)

    def __video_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.__video_player.setPosition(0)
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.__video_player.play()

    def __show_error(self):
        QMessageBox.warning(self, "No video to play", "Please add a video")

    def set_video_source(self, video: str):
        self.__video_player.setPosition(0)
        video_source = QUrl.fromLocalFile(video)
        QTimer.singleShot(150, partial(self.__video_player.setSource, video_source))

    def play(self):
        if self.__video_player.source() != "":
            if self.__video_player.isPlaying():
                self.__video_player.pause()
            else:
                self.__video_player.play()
        else:
            self.__show_error()

    def set_audio_output_volume(self, volume: float):
        self.__audio_output.setVolume(volume)

    def set_video_position(self, position: int):
        self.__video_player.setPosition(position)

    def get_video_player_state(self) -> QMediaPlayer.PlaybackState:
        return self.__video_player.playbackState()