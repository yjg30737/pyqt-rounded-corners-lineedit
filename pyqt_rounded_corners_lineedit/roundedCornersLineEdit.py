from PyQt5.QtWidgets import QLineEdit
from python_get_absolute_resource_path.getAbsoulteResourcePath import get_absolute_resource_path


class RoundedCornersLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initStyle()

    def __initStyle(self):
        css_file = open(get_absolute_resource_path('style/lineedit.css'))
        css_code = css_file.read()
        css_file.close()
        border_radius = self.sizeHint().height()/2
        padding = self.sizeHint().height()/5
        self.setStyleSheet(self.styleSheet() + css_code.format(border_radius, padding))

    def event(self, e):
        # catch font change event
        if e.type() == 97:
            self.__initStyle()
        return super().event(e)