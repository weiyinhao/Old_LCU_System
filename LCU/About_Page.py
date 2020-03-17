from PyQt5.Qt import *
from resource.about import Ui_Form
class About(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    #显示页面槽函数
    def showEvent(self, QShowEvent):
        self.setWindowTitle("聊城大学校历")
        pix = QPixmap(".//resource//img//20190822095245484490.jpg")
        self.label.setScaledContents(True)
        self.label.setPixmap(pix)
        pix2=QPixmap(".//resource//img//20190822095302735506.jpg")
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(pix2)