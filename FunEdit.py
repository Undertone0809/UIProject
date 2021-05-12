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
        #widget连接
        self.treeWidget.clicked.connect(lambda :self.onTreeClicked(1))
        self.treeWidget_2.clicked.connect(lambda :self.onTreeClicked(2))
        self.treeWidget_3.clicked.connect(lambda :self.onTreeClicked(3))

        self.setWindowIcon(QIcon("./images/folder_folder.png"))

    def onTreeClicked(self,num):
        item = self.treeWidget.currentItem()
        #获取当前序号
        index_top = self.treeWidget.indexOfTopLevelItem(item)
        #根据节点序号直接调用page页面
        if num==1:self.stackedWidget.setCurrentIndex(index_top)
        if num==2:self.stackedWidget_2.setCurrentIndex(index_top)




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

