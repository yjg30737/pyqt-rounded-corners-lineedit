from PyQt5.QtWidgets import QLineEdit


class RoundedCornersLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_file = open('style/lineedit.css')
        css_code = css_file.read()
        css_file.close()
        self.setStyleSheet(css_code.format(self.sizeHint().height()/2.5, self.sizeHint().height()/7))