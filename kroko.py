import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://www.google.com/"))
web.setWindowTitle("Kroko")
web.show()
app.exec_()