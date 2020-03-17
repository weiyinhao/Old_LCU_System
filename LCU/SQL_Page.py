from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.Qt import *

from resource.education_system import Ui_Form
from API.APT_Tool import APITool

class DBManager():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QODBC")
        self.db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=URPSYS;Uid=st;Pwd=123456")
        self._trytoConnect()
    #检测是否数据库正常打开
    def _trytoConnect(self):
        if self.db.open():
            print("数据库连接成功")
        else:
            print("数据库连接失败！")
    def student_insert_data(self,dic_list):

        self.query.exec_("insert into student values(dic_list)")
