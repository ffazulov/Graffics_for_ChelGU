from PyQt5 import QtCore, QtGui, QtWidgets
from modules import *
from MadeGif import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 700)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 471, 51))
        self.textEdit.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.textEdit.setObjectName("textEdit")
        self.creat_grafic_Button = QtWidgets.QPushButton(self.centralwidget)
        self.creat_grafic_Button.setGeometry(QtCore.QRect(430, 640, 171, 51))
        self.creat_grafic_Button.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 25px;\n"
"font: 25 14pt \"Microsoft YaHei Light\";")
        self.creat_grafic_Button.setObjectName("creat_grafic_Button")
        self.delet_grafic_Button = QtWidgets.QPushButton(self.centralwidget)
        self.delet_grafic_Button.setGeometry(QtCore.QRect(140, 640, 201, 51))
        self.delet_grafic_Button.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 25px;\n"
"font: 25 14pt \"Microsoft YaHei Light\";")
        self.delet_grafic_Button.setObjectName("delet_grafic_Button")
        self.create_gif_Button = QtWidgets.QPushButton(self.centralwidget)
        self.create_gif_Button.setGeometry(QtCore.QRect(700, 640, 181, 51))
        self.create_gif_Button.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 25px;\n"
"font: 25 14pt \"Microsoft YaHei Light\";")
        self.create_gif_Button.setObjectName("create_gif_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 980, 550))
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.frame.setStyleSheet("background-color: rgb(187, 255, 176);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progress_Bar = QtWidgets.QProgressBar(self.frame)
        self.progress_Bar.setGeometry(QtCore.QRect(650, 20, 341, 31))
        self.progress_Bar.setRange(0, 29700)
        self.progress_Bar.setProperty("value", 0)
        self.progress_Bar.setObjectName("progressBar")
        self.clear_text_Button = QtWidgets.QPushButton(self.frame)
        self.clear_text_Button.setGeometry(QtCore.QRect(500, 10, 131, 51))
        self.clear_text_Button.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius: 25px;\n"
"font: 25 14pt \"Microsoft YaHei Light\";")
        self.clear_text_Button.setObjectName("clear_text_Button")
        self.frame.raise_()
        self.textEdit.raise_()
        self.creat_grafic_Button.raise_()
        self.delet_grafic_Button.raise_()
        self.create_gif_Button.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.clear_textline()

        self.create_grafic()

        self.delit_grafic()

        self.create_gif()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Напишите слова через запятую, например (1слово, 2слово 2слово, 3 слово)</p></body></html>"))
        self.creat_grafic_Button.setText(_translate("MainWindow", "Создать график"))
        self.delet_grafic_Button.setText(_translate("MainWindow", "Уничтожить график"))
        self.create_gif_Button.setText(_translate("MainWindow", "Создать гифку"))
        self.clear_text_Button.setText(_translate("MainWindow", "Очистить"))

    def clear_textline(self):
        self.clear_text_Button.clicked.connect(self.clear_text)

    def delit_grafic(self):
        self.delet_grafic_Button.clicked.connect(self.delit)

    def delit(self):
        pixmap2 = QtGui.QPixmap("clear.png")
        self.label.setPixmap(pixmap2)
        self.label.setScaledContents(True)

        self.onProgress(0)

    def clear_text(self):
        self.textEdit.clear()

    def create_grafic(self):
        self.creat_grafic_Button.clicked.connect(self.my_code_create_grafic)

    def create_gif(self):
        self.create_gif_Button.clicked.connect(self.creat_gif)
        self.create_gif_Button.clicked.connect(self.dialog)

    def dialog(self):
        dig = QtWidgets.QDialog()
        dig.setStyleSheet('background-color: rgb(80, 80, 80);')
        dig.setFixedSize(640, 170)

        path = sys.path[0]
        dig.label = QtWidgets.QLabel(dig)
        dig.label.setGeometry(QtCore.QRect(0, 0, 631, 171))
        dig.label.setAlignment(QtCore.Qt.AlignCenter)
        dig.label.setObjectName("label")
        dig.label.setText(f'Ваша гифка уже сделана!\nГиф находиться тут: {path}\\result.gif')
        dig.exec_()



    def onProgress(self, val):
        self.progress_Bar.setValue(val)

    def my_code_create_grafic(self):
        text_user = self.textEdit.toPlainText()
        words_user = text_user.lower().split(', ')
        iteration = 0
        g = generator_txt()
        dir_words = {word: {} for word in words_user}
        for text_in_file, name in tqdm(g):
            iteration += 1
            self.onProgress(iteration)

            for word, dir_counts in dir_words.items():

                teg = f'\\b{word}\\b'

                mounth = name

                res = len(re.findall(teg, text_in_file))
                if mounth in dir_counts:
                    dir_counts[mounth] += res
                else:
                    dir_counts[mounth] = res

        for word, dir_counts in dir_words.items():
            list_mounth = ['Январь', 'февраль', 'март', 'апрель', 'июнь']

            lst_count_word = [dir_counts[munth] for munth in dir_counts]
            plt.plot(list_mounth, lst_count_word)
        plt.title(' '.join(words_user))
        plt.grid(True)
        plt.xlabel('Месяца')
        plt.ylabel('Количество')
        plt.legend(words_user)
        plt.savefig('saved_figure.png', )

        plt.close()

        pixmap = QtGui.QPixmap("saved_figure.png")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def creat_gif(self):
        g = generator_json()
        stopwords = stopwords_creat()
        stopwords.append('это')
        stopwords.append('который')
        dir_mounth = {}
        iteration = 0
        for text_in_file, name in tqdm(g):
            mounth = list(name)[6]
            iteration += 1
            if iteration%100==0:
                self.onProgress(iteration)
                # break

            text = dellit_symbols(text_in_file)
            text = norm_form_words(text)
            text = dellit_stopwords(text, stopwords)

            dir_result = append_in_dir(text)



            if mounth in dir_mounth:
                dir_mounth[mounth] = dir_plus_dir(dir_mounth[mounth], dir_result)
            else:
                dir_mounth[mounth] = dir_result

            text = ' '.join(text)
            saving_cleared_text(text, mounth, iteration)

        list_dirs = converting_dir_to_csv(dir_mounth)

        made_gif()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
