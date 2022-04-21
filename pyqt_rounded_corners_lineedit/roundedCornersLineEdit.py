from PyQt5.QtWidgets import QLineEdit


class RoundedCornersLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f'QLineEdit '
                           f'{{ '
                           f'border-radius: {self.sizeHint().height()/2.5}; '
                           f'padding: {self.sizeHint().height()/7}; '
                           f'}}')