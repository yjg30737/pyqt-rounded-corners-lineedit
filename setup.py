from setuptools import setup, find_packages

setup(
    name='pyqt-rounded-corners-lineedit',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_rounded_corners_lineedit.style': ['lineedit.css']},
    description='PyQt QLineEdit with rounded corners',
    url='https://github.com/yjg30737/pyqt-rounded-corners-lineedit.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)