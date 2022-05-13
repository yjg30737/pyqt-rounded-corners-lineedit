# pyqt-rounded-corners-lineedit
PyQt QLineEdit with rounded corners

## Requirements
* PyQt5 >= 5.8

## Install
`python -m pip install pyqt-rounded-corners-lineedit`

## Included Packages
* <a href="https://github.com/yjg30737/absresgetter.git">absresgetter</a> - To get absolute path of resource file

## Detailed Description
Rounded corners, borderless line edit.

If you want to add the border, add code like below.

`lineEdit.setStyleSheet(lineEdit.styleSheet() + 'QLineEdit { border: 1px solid black; }')`

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
from pyqt_rounded_corners_lineedit import RoundedCornersLineEdit


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lineEdit = RoundedCornersLineEdit()
        # if you want to set the border
        # lineEdit.setStyleSheet(lineEdit.styleSheet() + 'QLineEdit { border: 1px solid black; }')
        lay = QGridLayout()
        lay.addWidget(lineEdit)
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec_()
```

## Result

![image](https://user-images.githubusercontent.com/55078043/164461900-e212c0cc-9f62-4451-bd62-880614a7c074.png)



