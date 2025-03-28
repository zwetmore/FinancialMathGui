from PyQt5.QtWidgets import *
from models import *
from views import *


app = QApplication([])

home_page_window = HomePageWindow()

app.exec_()
