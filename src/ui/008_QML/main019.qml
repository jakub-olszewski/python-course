import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Przykład QML z Pythonem"

    Rectangle {
        width: parent.width
        height: parent.height

         Canvas {
             id: canvas
             anchors.fill: parent

             onPaint: {
                 var ctx = getContext("2d");

                 // Rysowanie prostokąta
                 ctx.fillStyle = "blue";
                 ctx.fillRect(50, 50, 100, 50);

                 // Rysowanie koła
                 ctx.beginPath();
                 ctx.arc(250, 75, 25, 0, 2 * Math.PI);
                 ctx.fillStyle = "red";
                 ctx.fill();
                 ctx.closePath();

                 // Rysowanie linii
                 ctx.beginPath();
                 ctx.moveTo(50, 350);
                 ctx.lineTo(150, 350);
                 ctx.strokeStyle = "green";
                 ctx.stroke();
                 ctx.closePath();
             }
         }


        TextField {
            id: textField
            anchors.centerIn: parent
            placeholderText: "Wpisz coś..."
            onTextChanged: backend.text = text
        }

        Button {
            text: "Pokaż"
            anchors.top: textField.bottom
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: backend.showMessage()
        }
    }
}
