import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,QTextBrowser,
                             QGridLayout,QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import  QIcon,QFont
from PyQt5.QtCore import QCoreApplication
import pymysql
from html.parser import HTMLParser




class Page_home(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,100,700,600)
        self.setWindowTitle('LeetCode')
        self.setWindowIcon(QIcon('LeetCode.png'))
        self.index_Button()
        self.show()

    def index_Button(self):

        self.index_start = QPushButton('START', self)
        self.index_start.clicked.connect(self.start)
        self.index_start.setFont(QFont('Castellar',26))

        self.index_quit = QPushButton('QUIT', self)
        self.index_quit.clicked.connect(QCoreApplication.instance().quit)
        self.index_quit.setFont(QFont('Castellar', 26))

        hbox = QVBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.index_start)
        hbox.addStretch(1)
        hbox.addWidget(self.index_quit)
        hbox.addStretch(1)

        vbox = QHBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def start(self):
        print("@@@@@@@@@@@@@@@@@@@@")
        self.close()
        d.show()




class Question_Page(QWidget):
    question_id = 647
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.show()

    def initUI(self):
        self.setGeometry(300,100,700,600)
        self.setWindowTitle('LeetCode')
        self.setWindowIcon(QIcon('LeetCode.png'))
        self.question_page()

    def question_page(self):
        # next question button
        self.question_next = QPushButton('next', self)
        self.question_next.clicked.connect(self.switch)
        self.question_next.setFixedSize(100, 50)
        self.question_next.setFont(QFont('Castellar', 14))

        #last question button
        self.question_back = QPushButton('back', self)
        self.question_back.clicked.connect(self.switch)
        self.question_back.setFixedSize(100, 50)
        self.question_back.setFont(QFont('Castellar', 14))

        # question description
        self.question = QTextBrowser(self)
        self.question.append(self.problemGet())
        self.question.setFont(QFont('Consolas',15))


        # home button
        self.home = QPushButton('',self)
        self.home.clicked.connect(self.start)
        self.home.setStyleSheet(" background-image:url(home.ico);border:none")
        self.home.setFixedSize(64,64)

        grid = QGridLayout()
        grid.setSpacing(100)
        grid.addWidget(self.question_next,2,1)
        grid.addWidget(self.question_back,2,0)
        grid.addWidget(self.home,1,1)
        grid.addWidget(self.question,1,0)

        self.setLayout(grid)

    def switch(self):
        if self.sender().text() == 'next':
            Question_Page.question_id += 1
        else:
            Question_Page.question_id -= 1
        self.question.setText(self.problemGet())
        print(Question_Page.question_id)

    def problemGet(self):
        a = DataBase()
        problem = a.findItem(Question_Page.question_id)
        a.close()
        return problem

    def start(self):
        print("@@@@@@@@@@@@@@@@@@@@")
        self.close()
        c.show()



class DataBase(object):

    def __init__(self):
        self.db = pymysql.connect("localhost","testuser","test123","leetcode")
        self.cursor = self.db.cursor()

    def findItem(self, idNum):
        sql = "select * from question where id = '%d' " %  (idNum)
        self.cursor.execute(sql)
        result = (self.cursor.fetchone())
        html_parser = HTMLParser()
        return html_parser.unescape(self.infoDeal(result))



    def infoDeal(self, r):
        s = []
        s.append('No.' + str(r[0])+' '+r[1])
        s.append('Difficulty: ' + ['Easy','Media','Hard'][r[3]-1])
        s.append('Description: ' + r[-1])
        return '\n'.join(s)


    def close(self):
        self.db.close()


app = QApplication(sys.argv)
c = Page_home()
d = Question_Page()
sys.exit(app.exec_())
