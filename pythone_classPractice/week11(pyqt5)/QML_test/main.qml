import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 1.4

import Example 1.0
import "qrc:/main.qml"

Window {
    width: 500
    height: 500
    visible: true

    ListView {
        anchors.fill: parent
        model: store.channels
        delegate: Item {
            anchors.left: parent.left
            anchors.right: parent.right
            height: 24
            Row {
                anchors.fill: parent
                Label {
                    text: name
                }
                Label {
                    text: title
                }
            }
        }
    }
}