from PyQt5.QtWidgets import*
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5 import uic
import sys



form_class = uic.loadUiType("movie.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.btn_add.clicked.connect(self.add)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_payment.clicked.connect(self.totalAmount)
        self.total_value = 0
        self.current_titles = []
        self.current_tickets = {}

    def add(self):
        ticket1 = self.count_ticket1
        ticket2 = self.count_ticket2
        ticket3 = self.count_ticket3
        ticket4 = self.count_ticket4
        ticket5 = self.count_ticket5
        ticket6 = self.count_ticket6
        #체크
        ticket_count = [ticket1.text(), ticket2.text(), ticket3.text(), ticket4.text(), ticket5.text(), ticket6.text()]
        tickets = [ticket1, ticket2, ticket3, ticket4, ticket5, ticket6]

        movieName1 = self.label_2.text()
        movieName2 = self.label_3.text()
        movieName3 = self.label_4.text()
        movieName4 = self.label_5.text()
        movieName5 = self.label_6.text()
        movieName6 = self.label_7.text()
        movieNames = [movieName1, movieName2, movieName3, movieName4,movieName5, movieName6]

        # self.list_payment.model().removeRow(0)


        for i in range(6):
        # 2를 지우고 5, 2를 5로 바꾸기
            if len(ticket_count[i]) >= 1 and ticket_count[i].isdigit() == True:
                self.total_value = self.total_value + (int(ticket_count[i])) * 14000
                self.total.setText(str(self.total_value))
                print(movieNames[i], ticket_count[i])

                if movieNames[i] in self.current_titles:
                    self.list_payment_2.model().removeRow(i)
                    self.current_tickets[movieNames[i]] += int(ticket_count[i])
                    print(self.current_tickets, self.current_tickets[movieNames[i]])
                    self.list_payment_2.insertItem(i, str(self.current_tickets[movieNames[i]]))

                else:
                    self.current_titles.append(movieNames[i])
                    self.current_tickets[movieNames[i]] = int(ticket_count[i])
                    self.list_payment.addItem(movieNames[i])
                    self.list_payment_2.addItem(ticket_count[i])

                tickets[i].clear()

            elif ticket_count[i].isdigit() == False:
                tickets[i].clear()
        print(self.current_titles)
        print(self.current_tickets.values())



    def clear(self):
        self.list_payment.clear()
        self.list_payment_2.clear()
        self.total_value = 0
        self.total.setText('0')
        self.current_tickets.clear()
        self.current_titles.clear()


    def totalAmount(self, event):

        try:
            reply = QMessageBox.question(self, 'Message', f'총 금액{self.total_value}원 입니다. 결제 하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                QMessageBox.about(self, 'Title.', '완료되었습니다.')
                self.list_payment.clear()
                self.list_payment_2.clear()
                self.total_value = 0
                self.total.setText('0')
                self.current_tickets.clear()
                self.current_titles.clear()
            else:
                    event.ignore()
        except:
            pass








if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


