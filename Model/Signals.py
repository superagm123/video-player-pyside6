from PySide6.QtCore import Signal, QObject

class VideoPlayerSignals(QObject):
    videoDurationChanged = Signal(int)
    videoPositionChanged = Signal(int)
    videoStateChanged = Signal(object)