from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import *
from MainActivity import Ui_Form

class MainOperate(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # 往空的QWidget里面放置UI内容
        self.setupUi(self)
        self.init()
        self.init_setIcon()


    def init(self):
        self.treeWidget.itemClicked.connect(self.click_firstButton)
        self.setWindowIcon(QIcon("./images/folder_folder.png"))


    def init_setIcon(self):
        #self.treeWidget.setIcon(QIcon('./images/folder_folder.png'))
        pass

    def click_firstButton(self,item,column):
        print(item.text(column))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = MainOperate()
    Form.show()
    sys.exit(app.exec_())

