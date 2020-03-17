from PyQt5.Qt import *
import PyQt5.sip
from Login_Page import LoginPane
from Education_system_Page import Edt_sys
import PyQt5.sip
import qdarkstyle
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    login_pane = LoginPane()#登录窗口
    login_pane.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Edt_sys_pane = Edt_sys()#主页面

    #定义槽函数
    def success_login_slot():
        #隐藏当前窗口
        login_pane.hide()
        #展示查询窗口
        Edt_sys_pane.show()

    #绑定信号和槽(登录成功信号会发送到槽函数里)
    login_pane.success_login.connect(success_login_slot)

    sys.exit(app.exec_())