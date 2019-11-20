import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from main_ui import Ui_MainWindow1
from addEditCoffeeForm import Ui_MainWindow2

class Coffee(Ui_MainWindow1, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.view()
        self.info.clicked.connect(self.print_info)
        self.add.clicked.connect(self.addEdit)
        self.change.clicked.connect(self.addEdit)

    def view(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        titles = cur.execute("""SELECT title FROM coffee""").fetchall()
        for i in titles:
            self.sortbox.addItem(str(i[0]))
        con.close()

    def print_info(self):
        title = self.sortbox.currentText()
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        info = cur.execute("""SELECT * FROM coffee WHERE title = '{}'""".format(title)).fetchall()[0]
        con.close()

        self.id.setText(f'ID продукта: {info[0]}')
        self.roast.setText(f'Степень обжарки: {info[2]}')
        self.ground.setText(f'{info[3]}')
        self.taste.setText(f'{info[4]}')
        self.price.setText(f'Цена: {info[5]} руб.')
        self.volume.setText(f'Объем упаковки: {info[6]} г.')

    def addEdit(self):
        global nc
        nc = NewCoffee(self, self.sender().text(), self.sortbox.currentText())
        nc.show()


class NewCoffee(Ui_MainWindow2, QMainWindow):
    def __init__(self, parent, b, old_title):
        super().__init__()
        self.old_title = old_title
        self.parent = parent
        self.setupUi(self)
        if b == 'Добавить новый':
            self.setWindowTitle('Создание')
            self.info.setText('Добавить новую запись о кофе')
            self.save.clicked.connect(self.add_coffee)
        elif b == 'Изменить':
            self.setWindowTitle('Изменение')
            self.info.setText('Изменить запись о кофе')
            con = sqlite3.connect("data/coffee.sqlite")
            cur = con.cursor()
            info = cur.execute("""SELECT * FROM coffee WHERE title = '{}'""".format(self.old_title)).fetchall()[0]
            con.close()
            # print info
            self.title.setText(f'{info[1]}')
            self.roast.setText(f'{info[2]}')
            self.ground.setText(f'{info[3]}')
            self.taste.setText(f'{info[4]}')
            self.price.setText(f'{info[5]}')
            self.volume.setText(f'{info[6]}')
            self.save.clicked.connect(self.edit_coffee)

    def add_coffee(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        # added coffee
        if (len(self.title.toPlainText()) != 0) and (len(self.roast.toPlainText()) != 0) \
                and (len(self.ground.toPlainText()) != 0) and (len(self.taste.toPlainText()) != 0) \
                and (len(self.price.toPlainText()) != 0) and (len(self.volume.toPlainText()) != 0):
            cur.execute("""INSERT INTO coffee(title) VALUES('{}')""".format(self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET roast = '{}' WHERE title = '{}'""".format(self.roast.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET ground = '{}' WHERE title = '{}'""".format(self.ground.toPlainText(),
                                                                                        self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET taste = '{}' WHERE title = '{}'""".format(self.taste.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET price = '{}' WHERE title = '{}'""".format(self.price.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET volume = '{}' WHERE title = '{}'""".format(self.volume.toPlainText(),
                                                                                        self.title.toPlainText())).fetchall()
            con.commit()
            con.close()
            self.parent.sortbox.clear()
            self.parent.view()
            self.close()
        else:
            self.info_2.setText('Все поля должны быть заполнены!')


    def edit_coffee(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        # changed info
        if (len(self.title.toPlainText()) != 0) and (len(self.roast.toPlainText()) != 0) \
                and (len(self.ground.toPlainText()) != 0) and (len(self.taste.toPlainText()) != 0) \
                and (len(self.price.toPlainText()) != 0) and (len(self.volume.toPlainText()) != 0):
            cur.execute("""UPDATE coffee SET title = '{}' WHERE title = '{}'""".format(self.title.toPlainText(),
                                                                                        self.old_title)).fetchall()
            cur.execute("""UPDATE coffee SET roast = '{}' WHERE title = '{}'""".format(self.roast.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET ground = '{}' WHERE title = '{}'""".format(self.ground.toPlainText(),
                                                                                        self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET taste = '{}' WHERE title = '{}'""".format(self.taste.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET price = '{}' WHERE title = '{}'""".format(self.price.toPlainText(),
                                                                                       self.title.toPlainText())).fetchall()
            cur.execute("""UPDATE coffee SET volume = '{}' WHERE title = '{}'""".format(self.volume.toPlainText(),
                                                                                        self.title.toPlainText())).fetchall()
            con.commit()
            con.close()
            self.parent.sortbox.clear()
            self.parent.view()
            self.close()
        else:
            self.info_2.setText('Все поля должны быть заполнены!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
