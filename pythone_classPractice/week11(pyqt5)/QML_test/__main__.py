from sys import argv
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QTimer, pyqtProperty, pyqtSignal
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine, qmlRegisterType
                
class Channel(QObject):

    nameChanged = pyqtSignal()
    titleChanged = pyqtSignal()

    def __init__(self, name='', title='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._title = title

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name != self._name:
            self._name = name
            self.nameChanged.emit()
            
    @pyqtProperty('QString', notify=nameChanged)
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title != self._title:
            self._title = title
            self.titleChanged.emit()

class Store(QObject):

    channelsChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._channels = [
            Channel('aa', 'AAA'),
            Channel('bb', 'BBB')
        ]

    @pyqtProperty(QQmlListProperty, notify=channelsChanged)
    def channels(self):
        return QQmlListProperty(Channel, self, self._channels)

    @channels.setter
    def channels(self, channels):
        if channels != self._channels:
            self._channels = channels
            self.channelsChanged.emit()

    def appendChannel(self, channel):
        self._channels.append(channel)
        self.channelsChanged.emit()


def main():
    app = QApplication(argv)

    qmlRegisterType(Channel, 'Example', 1, 0, 'Channel')
    qmlRegisterType(Store, 'Example', 1, 0, 'Store')

    store = Store()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('store', store)
    engine.load('main.qml')

    # After 3 seconds, we append a new Channel
    QTimer.singleShot(3000, lambda: store.appendChannel(Channel('cc', 'CCC')))

    exit(app.exec_())


if __name__ == '__main__':
    main()