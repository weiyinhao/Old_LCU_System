from PyQt5.Qt import *
from resource.about_Reissue_certificate import Ui_Form
class About_Reissue(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    #显示页面槽函数
    def showEvent(self, QShowEvent):
        self.setWindowTitle("关于补办证明")
        pix = QPixmap(".//resource//img//20190426080818487152.png")
        self.label.setPixmap(pix)