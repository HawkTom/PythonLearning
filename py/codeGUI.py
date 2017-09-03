import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,QTextBrowser,
                             QGridLayout,QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import  QIcon,QFont
from PyQt5.QtCore import QCoreApplication
import pymysql
from html.parser import HTMLParser


class Page_index(QWidget):
    question_id = 647

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300,100,700,600)
        self.setWindowTitle('LeetCode')
        self.setWindowIcon(QIcon('LeetCode.png'))
        # self.index_Button()
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



    def question_page(self):
        # next question button
        self.question_next = QPushButton('next', self)
        self.question_next.clicked.connect(self.switch)
        self.question_next.setGeometry(550,500,100,50)
        self.question_next.setFont(QFont('Castellar', 14))

        #last question button
        self.question_back = QPushButton('back', self)
        self.question_back.clicked.connect(self.switch)
        self.question_back.setGeometry(70, 500, 100, 50)
        self.question_back.setFont(QFont('Castellar', 14))

        # question description
        self.question = QTextBrowser(self)
        self.question.append(self.problemGet())
        self.question.setFont(QFont('Consolas',10))
        self.question.resize(self.width()*0.8, self.height()*0.5)
        self.question.move(50,50)

        # home button
        self.home = QPushButton('',self)
        self.home.clicked.connect(self.start1)
        self.home.setStyleSheet(" background-image:url(home.ico);border:none")
        self.home.setGeometry(600, 30, 64, 64)

        # layout
        grid = QHBoxLayout()
        grid.addStretch(1)
        grid.addWidget(self.question_next)
        grid.addStretch(1)
        grid.addWidget(self.question_back)
        grid.addStretch(1)
        grid.addWidget(self.home)
        grid.addStretch(1)
        grid.addWidget(self.question)
        grid.addStretch(1)

        self.setLayout(grid)




    def start(self):
        print("@@@@@@@@@@@@@@@@@@@@")
        self.index_start.close()
        self.index_quit.close()
        self.question_page()
        self.question.show()
        self.question_next.show()
        self.question_back.show()
        self.home.show()


    def start1(self):
        self.index_start.show()
        self.index_quit.show()
        self.question.close()
        self.question_next.close()
        self.question_back.close()
        self.home.close()

    def switch(self):
        if self.sender().text() == 'next':
            Page_index.question_id += 1
        else:
            Page_index.question_id -= 1
        self.question.setText(self.problemGet())
        print(Page_index.question_id)


    def problemGet(self):
        a = DataBase()
        problem = a.findItem(Page_index.question_id)
        a.close()
        return problem

# class Question_Page(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,100,700,600)
#         self.setWindowTitle('LeetCode')
#         self.setWindowIcon(QIcon('LeetCode.png'))
#         self.index_Button()
#         self.show()


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
w = Page_index()
sys.exit(app.exec_())
