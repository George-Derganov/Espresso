import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        self.view()
        self.info.clicked.connect(self.print_info)

    def view(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        titles = cur.execute("""SELECT title FROM coffee""").fetchall()
        for i in titles:
            self.sortbox.addItem(i[0])
        con.close()

    def print_info(self):
        title = self.sortbox.currentText()
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        info = cur.execute("""SELECT * FROM coffee WHERE title = '{}'""".format(title)).fetchall()[0]
        con.close()

        self.id.setText(f'ID продукта: {info[0]}')
        self.roast.setText(f'Степень обжарки: {info[2]}')
        self.ground.setText(info[3])
        self.taste.setText(info[4])
        self.price.setText(f'{info[5]} руб.')
        self.volume.setText(f'{info[6]} г.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
