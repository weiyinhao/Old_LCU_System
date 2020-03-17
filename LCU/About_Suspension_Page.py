from PyQt5.Qt import *
from resource.about_Suspension import Ui_Form
class About_Suspension(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    #显示页面槽函数
    def showEvent(self, QShowEvent):
        self.setWindowTitle("关于休学")
        pix=QPixmap(".//resource//img//20190426080906997358.png")
        self.label.setPixmap(pix)
