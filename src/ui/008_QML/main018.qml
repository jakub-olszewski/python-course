import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Przykład QML"

    Button {
        text: "Kliknij mnie!"
        onClicked: console.log("Przycisk został kliknięty!")
    }
}
