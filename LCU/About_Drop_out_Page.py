from PyQt5.Qt import *
from resource.about_Drop_out import Ui_Form
class About_Drop_out(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    #显示页面槽函数
    def showEvent(self, QShowEvent):
        self.setWindowTitle("关于退学")
        pix = QPixmap(".//resource//img//20190426080849127234.png")
        self.label.setPixmap(pix)