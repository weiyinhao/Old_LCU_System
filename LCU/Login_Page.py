from PyQt5.Qt import *
from resource.login import Ui_Form
from API.APT_Tool import APITool

class LoginPane(QWidget,Ui_Form):
    #登录成功后发送
    success_login=pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.refresh_yzm()
        # 禁止窗口最大化和拖动
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.width(), self.height())
    #刷新验证码
    def refresh_yzm(self):
        url=APITool.download_yzm()
        self.currentUrl=url
        pixmp=QPixmap(url)
        self.yzm_label.setPixmap(pixmp)
    #登录
    def check_login(self):
        account=self.account_led.text()
        pwd=self.psw_led.text()
        yzm=self.yzm_led.text()
        if not APITool.Login(account,pwd,yzm):
            print("登录失败！请重新尝试")
            QMessageBox.warning(self, "提示", "登录失败，请重新尝试！\n可能原因:1.账号密码错误 2.无法链接服务器")
            self.refresh_yzm()
            return None
        else:
            print("登录成功")
            self.success_login.emit()
    #更换验证码
    def replace_yzm(self):
        self.refresh_yzm()
    #重置信息
    def Reset_info(self):
        self.account_led.clear()
        self.psw_led.clear()
        self.yzm_led.clear()
    #找回密码
    def recover_pwd(self):
        QMessageBox.warning(self, "提示", "教务系统暂不支持该请求！")
        return None
    #输入框内容是否为空
    def Led_is_text(self):
        #获取三个输入框的内容
        account=self.account_led.text()
        psw=self.psw_led.text()
        yzm=self.yzm_led.text()
        if len(account) == 0 or len(psw) == 0 or len(yzm) == 0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)

    login=LoginPane()

    login.show()

    sys.exit(app.exec_())