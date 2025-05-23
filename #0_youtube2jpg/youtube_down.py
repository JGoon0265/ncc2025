# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_down.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 166)
        Form.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* 어두운 배경색 */
            font-family: Arial, sans-serif;
            font-size: 12pt;
            color: white;  /* 글자 색을 흰색으로 설정 */
        }
        QLabel {
            color: #FFFFFF;  /* 레이블 텍스트 색상 */
        }
        QLineEdit {
            background-color: #444444;  /* 어두운 회색 배경 */
            color: white;  /* 텍스트 색상 흰색 */
            border: 1px solid #888888;  /* 테두리 색상 */
            padding: 5px;
            border-radius: 5px;  /* 둥근 모서리 */
        }
        QRadioButton {
            color: white;  /* 라디오 버튼 텍스트 색상 */
        }
        QPushButton {
            background-color: #5C5C5C;  /* 버튼 배경색 어두운 회색 */
            color: white;  /* 버튼 텍스트 색상 흰색 */
            border: 1px solid #888888;  /* 버튼 테두리 색상 */
            padding: 5px;
            border-radius: 5px;  /* 둥근 모서리 */
        }
        QPushButton:hover {
            background-color: #4C4C4C;  /* 버튼에 마우스를 올렸을 때 색상 변화 */
        }
        QPushButton:pressed {
            background-color: #3C3C3C;  /* 버튼을 클릭했을 때 색상 변화 */
        }
        QRadioButton:checked {
            color: #33CC33;  /* 선택된 라디오 버튼 색상 (초록색) */
        }
    """)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 15, 200, 16))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 229, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 35, 361, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "유튜브 다운로더"))
        self.label.setText(_translate("Form", "동영상 URL/Filename"))
        self.radioButton_2.setText(_translate("Form", "프레임 캡쳐"))
        self.radioButton.setText(_translate("Form", "영상 다운로드"))
        self.pushButton.setText(_translate("Form", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
