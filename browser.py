from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
	def __init__(self):
		super().__init__()

		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("http://www.google.com"))

		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)

		self.back_button = QPushButton("back")
		self.back_button.clicked.connect(self.browser.back)

		self.forward_button = QPushButton("forward")
		self.forward_button.clicked.connect(self.browser.forward)

		self.refresh_button = QPushButton("refresh")
		self.refresh_button.clicked.connect(self.browser.reload)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.url_bar)
		self.layout.addWidget(self.back_button)
		self.layout.addWidget(self.forward_button)
		self.layout.addWidget(self.refresh_button)
		self.layout.addWidget(self.browser)

		self.container = QWidget()
		self.container.setLayout(self.layout)

		self.setCentralWidget(self.container)
		self.showMaximized()

	def navigate_to_url(self):
		url = self.url_bar.text()

		if not url.startswith("http://") and not url.startswith("https://"):
			url = "http://" + url

		self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	browser = Browser()
	sys.exit(app.exec_())
