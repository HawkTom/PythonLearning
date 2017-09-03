import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QToolTip,QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))  # 鼠标提示文字字体
		self.setToolTip('This is a <b>QWidget</b> widget') # 窗口提示文字

		btn = QPushButton('Button',self) # 添加按钮组件
		btn.setToolTip('This is a <b>QPushButton</b> widget') # 按钮提示文字
		btn.resize(btn.sizeHint()) # 设置按钮尺寸为推荐
		btn.move(50,50) # 按钮在窗口中的位置

		qbtn = QPushButton('Quit',self)
		qbtn.clicked.connect(QCoreApplication.instance().quit) # 信号连接
		qbtn.resize(btn.sizeHint())
		qbtn.move(150,50)



		self.setGeometry(300, 300, 300,220) # 窗口尺寸即位置
		self.setWindowTitle('Icon') # 窗口左上角名称
		self.setWindowIcon(QIcon('b.ico')) # 窗口应用图标

		self.show()

	def closeEvent(self, event): #重定义关闭窗口事件

		reply = QMessageBox.question(self, 'Message',
									 "Are you sure to quit?", QMessageBox.Yes |
									 QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

app = QApplication(sys.argv)
ex = example()
sys.exit(app.exec_())
