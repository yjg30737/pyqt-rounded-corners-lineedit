from PyQt5.QtWidgets import QLineEdit
from python_get_absolute_resource_path.getAbsoulteResourcePath import get_absolute_resource_path


class RoundedCornersLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_file = open(get_absolute_resource_path('style/lineedit.css'))
        css_code = css_file.read()
        css_file.close()
        border_radius = self.sizeHint().height()/2.5
        padding = self.sizeHint().height()/7
        self.setStyleSheet(css_code.format(border_radius, padding))