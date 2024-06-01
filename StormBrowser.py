import sys
from sys import argv as argv

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Window(QMainWindow):
  def __init__(self, *args, **kwargs):
     super(Window, self).__init__(*args, **kwargs)

     self.setStyleSheet("background-color: azure;")
     self.setWindowIcon(QtGui.QIcon('imgs/storm.png'))
     self.setFixedSize(900,800)

     #Toolbar 'NAVIGATION'...
     
     self.browser = QWebEngineView()
     self.browser.setUrl(QUrl('https://www.google.com'))
     self.browser.urlChanged.connect(self.update_AddressBar)
     self.setCentralWidget(self.browser)

     self.status_bar = QStatusBar()
     self.setStatusBar(self.status_bar)

     self.navigation_bar = QToolBar('Navigation Toolbar')
     self.addToolBar(self.navigation_bar)
     
     back_button = QAction("<", self)
     back_button.setStatusTip('Go to previous page you visited')
     back_button.triggered.connect(self.browser.back)
     self.navigation_bar.addAction(back_button)

     next_button = QAction(">", self)
     next_button.setStatusTip('Go to next page')
     next_button.triggered.connect(self.browser.forward)
     self.navigation_bar.addAction(next_button)

     refresh_button = QAction("⟳", self)
     refresh_button.setStatusTip('Refresh this page')
     refresh_button.triggered.connect(self.browser.reload)
     self.navigation_bar.addAction(refresh_button)

     home_button = QAction("🏠", self)
     home_button.setStatusTip('Go to home page (Google page)')
     home_button.triggered.connect(self.go_to_home)
     self.navigation_bar.addAction(home_button)

     self.navigation_bar.addSeparator()

     self.URLBar = QLineEdit()
     self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))  # This specifies what to do when enter is pressed in the Entry field
     self.navigation_bar.addWidget(self.URLBar)

     self.addToolBarBreak()

     #ToolBar 'BOOKMARKS'...
     
     bookmarks_toolbar = QToolBar('Bookmarks', self)
     self.addToolBar(bookmarks_toolbar)

     facebook = QAction("Facebook", self)
     facebook.setStatusTip("Go to Facebook")
     facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
     bookmarks_toolbar.addAction(facebook)

     instagram = QAction("Instagram", self)
     instagram.setStatusTip("Go to Instagram")
     instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
     bookmarks_toolbar.addAction(instagram)

     X = QAction("X", self)
     X.setStatusTip('Go to X')
     X.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
     bookmarks_toolbar.addAction(X)

     yt = QAction("YouTube", self)
     yt.setStatusTip('Go to YouTube')
     yt.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.youtube.com")))
     bookmarks_toolbar.addAction(yt)

     gm = QAction("Gmail", self)
     gm.setStatusTip('Go to Gmail')
     gm.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.gmail.com")))
     bookmarks_toolbar.addAction(gm)

     psg = QAction("PSGCAS", self)
     psg.setStatusTip('Go to PSGCAS')
     psg.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.psgcas.ac.in")))
     bookmarks_toolbar.addAction(psg)

     self.show()

  def go_to_home(self):
     self.browser.setUrl(QUrl('https://www.google.com/'))

  
    
  def go_to_URL(self, url: QUrl):
     if url.scheme() == '':
        url.setScheme('https://')
     self.browser.setUrl(url)
     self.update_AddressBar(url)

  def update_AddressBar(self, url):
     self.URLBar.setText(url.toString())
     self.URLBar.setCursorPosition(0)

def main():
     app = QApplication(argv)
     app.setApplicationName('Storm Browser')
     window = Window()
     app.exec_()

if __name__=='__main__':
   main()
     

# Developed by @lavanyan

