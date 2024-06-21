import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt

#pip install PyQt5 PyQtWebEngine

class BrowserWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://ya.ru/"))
        self.setCentralWidget(self.browser)
        # Создаем панель инструментов
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        # Создаем поле для ввода URL
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)
        # Кнопка "Назад"
        back_button = QAction('Назад', self)
        back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_button)
        # Кнопка "Вперед"
        forward_button = QAction('Вперед', self)
        forward_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_button)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
app = QApplication(sys.argv)
window = BrowserWindow()
window.show()
sys.exit(app.exec_())
