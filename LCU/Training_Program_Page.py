from PyQt5.Qt import *
from resource.trainingprogram import Ui_Form
from API.APT_Tool import APITool
class TraPro(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
    #初始化
    def Init(self):
        self.treeWidget.clicked.connect(self.get_clicked_info)
    #显示窗口的槽函数
    def showEvent(self, QShowEvent):
        dic_res, url_at_res = APITool.get_Trapro_info()
        #设置treewidget控件
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabel('课组信息')
        #添加相关课组信息
        for i in range(len(dic_res.keys())):
            root = QTreeWidgetItem(self.treeWidget)  # 根节点
            root.setText(0, list(dic_res.keys())[i])
            for j in range(len(list(dic_res.values())[i])):
                child=QTreeWidgetItem(root)
                child.setText(0,list(dic_res.values())[i][j])
        #全部展开
        #self.treeWidget.setItemsExpandable(False)
        self.treeWidget.expandAll()
    def get_clicked_info(self):
        dic_res, url_at_res = APITool.get_Trapro_info()
        clicked_item_text=self.treeWidget.currentItem().text(0)#获取点击的内容
        if clicked_item_text not in url_at_res.keys():
            return None
        url_res_values=url_at_res[clicked_item_text]
        course_info,Course_plan_info=APITool.get_course_group_info(url_res_values)
        #设置相关标签内容
        self.coursenumber.setText(course_info[0])
        self.coursename.setText(course_info[1])
        self.englishcoursename.setText(course_info[2])
        self.Coursedepartment.setText(course_info[3])
        self.Researchlogo.setText(course_info[4])
        self.credit.setText(course_info[5])
        self.Classhour.setText(course_info[6])
        self.Startdata.setText(course_info[8])
        self.Enddate.setText(course_info[9])
        self.coursestatus.setText(course_info[10])
        self.Inclassweektime.setText(course_info[11])
        self.Totalclasshours.setText(course_info[12])
        self.Designtotalhours.setText(course_info[13])
        self.Experimentaltotalhours.setText(course_info[14])
        self.Midtermtotalcomputerhours.setText(course_info[15])
        self.Discussioncounselingtotalhours.setText(course_info[16])
        self.Designassignmenttotalhours.setText(course_info[17])
        self.Extracurriculartotalhours.setText(course_info[18])
        self.Extracurricularcredits.setText(course_info[19])
        self.cousertype.setText(course_info[20])
        self.teachingmethods.setText(course_info[21])
        self.teachnumber.setText(course_info[22])
        self.teachingmaterial.setText(course_info[23])
        self.referencebook.setText(course_info[24])
        self.Faculty.setText(course_info[25])
        self.Coursedescription.setText(course_info[26])
        self.Testtype.setText(course_info[27])
        self.Campus.setText(course_info[28])
        self.briefintroduction.setText(course_info[29])
        self.Remarks.setText(course_info[30])

        #设置方案课程信息
        self.Plannedschoolyear.setText(Course_plan_info[0])
        self.Plansemester.setText(Course_plan_info[1])
        self.Courseattribute.setText(Course_plan_info[2])
        self.Testtype2.setText(Course_plan_info[3])

