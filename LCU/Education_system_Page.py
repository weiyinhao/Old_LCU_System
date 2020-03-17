from PyQt5.Qt import *
from resource.education_system import Ui_Form
from API.APT_Tool import APITool
import re
from Training_Program_Page import TraPro
from About_Page import About
from About_Drop_out_Page import About_Drop_out
from About_Reissue_certificate_Page import About_Reissue
from About_return_to_school_page import About_return_school
from About_Suspension_Page import About_Suspension
#定义学分绩点的子线程
class Gradepoint(QThread):
    rep_res_signal=pyqtSignal(str,list,list,dict)
    def run(self):
        grade_point_value, grade_point_res, start_or_end_academic_term_res,academic_term_dic = APITool.Check_Group_Point()
        self.rep_res_signal.emit(grade_point_value, grade_point_res, start_or_end_academic_term_res, academic_term_dic)
#定义查询指定期间绩点的子线程
class FixedTimerGradepoint(QThread):
    rep_res_signal = pyqtSignal(str)
    def run(self):
        academic_term_dic = APITool.Check_Group_Point()[3]
        start_timer = academic_term_dic[self.start_cmbox.currentText()]
        end_timer = academic_term_dic[self.end_cmbox.currentText()]
        res = APITool.query_fixed_timer_Group_Point(start_timer,end_timer)
        self.rep_res_signal.emit(res)

class Edt_sys(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.init()
        #禁止窗口最大化和拖动
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.width(),self.height())
        self.TraPro_page = TraPro()
        self.About_page=About()
        self.About_Drop_out_page=About_Drop_out()
        self.About_Reissue_page=About_Reissue()
        self.About_return_school_page=About_return_school()
        self.About_Suspension_page=About_Suspension()
    #初始化(例如 信号绑定等)
    def init(self):
        self.tabWidget.currentChanged.connect(self.Main_Page)#主页面
        self.tabWidget_2.currentChanged.connect(self.Select_course)#选课管理页面
        self.tabWidget_3.currentChanged.connect(self.Evaluate_Page)#教学评估页面
        self.tabWidget_4.currentChanged.connect(self.Grade_query_Page)#查询成绩页面
        self.tabWidget_5.currentChanged.connect(self.Education_resources_Page)#教学资源页面
        self.scool_year_lwid.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
    #个人照片信息
    def img_info(self):
        url=APITool.download_Img_info()
        self.currentUrl = url
        pixmp = QPixmap(url)
        self.Img_lab.setPixmap(pixmp)

    # 获取个人信息
    def personal_info(self):
        res,info = APITool.check_self_info()
        self.info_ted.clear()#每次点击都先把原先的内容清空
        for key in res:
            self.info_ted.append(key+" : "+res[key]+"\n")
        self.plan_btn.setText(info)
    #修改按钮
    def alter_info(self):
        QMessageBox.warning(self, "提示", "学籍临时库开关已关闭,不允许修改学籍信息！")
        return None
    #错误页面
    def Error_Page(self,lab):
        lab.setText("*对不起、非选课阶段不允许选课")
    #正确页面
    def Correct_Page(self,lab,string="选中课程"):
        lab.setText(string)
    #删除控件
    def Delect_kj(self,lab):
        lab.deleteLater()
    #个人培养方案
    def Training_program(self):
        #QMessageBox.warning(self, "提示", "待更新！")
        self.TraPro_page.show()# 显示培养页面
        #dic_res, url_at_res = APITool.get_Trapro_info()
        #return None
    #教学评估页面切换的槽函数
    def Evaluate_Page(self,index):
        if index==0:#评估公告
            pass
        elif index==1:#教学评估
            self.teacher_assess()
        elif index==2:#毕业生评估
            pass
    #选课管理页面切换标签的槽函数
    def Select_course(self,index):
        if index==0:#网上选课
            if not APITool.Net_select_course():
                self.Error_Page(self.label)
                return None
            self.Correct_Page(self.label)  # 设置正确页面信息标签
            #self.Delect_kj(self.label)
            #self.show_elective_course_page()
            pass#待教务处更新请求
        elif index==1:#选课结果
            timer_lab = APITool.Class_Schedule()[0]
            self.timer_lab.setText(timer_lab)
            self.Course_data(self.course_view_2,self.details_view_2)
        elif index==2:#退课
            if not APITool.Drop_course():
                self.Error_Page(self.label_4)#设置错误页面信息标签
                return None
            self.Correct_Page(self.label_4)#设置正确页面信息标签
            self.Set_drop_course_data(self.drop_course_view)#进行数据处理
            #self.Delect_kj(self.label_4)
        elif index==3:#无效的选课结果
            if not APITool.Null_Course():
                self.Error_Page(self.label_3)#设置错误页面信息标签
                return None
            self.Correct_Page(self.label_3,"无效选课结果")  # 设置正确页面信息标签
            self.set_null_course_data(self.null_course_res_view)#进行数据处理
            #self.Delect_kj(self.label_3)
        elif index==4:#本学期课表
            timer_lab=APITool.Class_Schedule()[0]
            self.timer_lab_2.setText(timer_lab)
            self.Course_data(self.course_view,self.details_view)
    #设置无效选课信息数据
    def set_null_course_data(self,view):
        headers, res_list = APITool.Null_Course()
        model = QStandardItemModel(view)
        model.setColumnCount(len(headers))
        for idx, title in enumerate(headers):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        view.setModel(model)
        #退课信息待获取........
    #设置退课信息数据
    def Set_drop_course_data(self,view):
        headers,res_list = APITool.Drop_course()
        model = QStandardItemModel(view)
        model.setColumnCount(len(headers))
        for idx,title in enumerate(headers):#设置退课视图的数据头
            model.setHeaderData(idx,Qt.Horizontal,title)
        #设置相关退课信息
        for row in range(len(res_list)//len(headers)):
            for colnum in range(len(headers)):
                model.setItem(row, colnum, QStandardItem(res_list[row * len(headers) + colnum]))
        view.setModel(model)
        self.In_the_view_btn(view,len(res_list)//len(headers),0,"删除");
    #本学期课程表数据
    def Course_data(self,course_view,course_view_info=None):
        timer_lab,res,res_info = APITool.Class_Schedule()#获取课表信息
        model = QStandardItemModel(course_view)
        model_info=QStandardItemModel(course_view_info)
        headers1=["节次","星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
        headers2 = ["培养方案", "课程号", "课程名", "课序号", "学分", "课程属性", "考试类型", "教师","大纲日历","修读方式","选课状态","周次","星期","节次","节数","校区","教学楼","教室"]
        model.setColumnCount(len(headers1))
        model_info.setColumnCount(len(headers2))
        for idx, title in enumerate(headers1):#设置课程数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for idx,title in enumerate(headers2):#设置课程信息数据头
            model_info.setHeaderData(idx, Qt.Horizontal, title)
        # 设置课程信息
        for row in range(10):
           for colnum in range(len(headers1)):
                model.setItem(row,colnum,QStandardItem(res[row*len(headers1)+colnum]))
        course_view.setModel(model)
        #设置课表信息列宽
        course_view.setColumnWidth(0,152)
        #设置列表只读
        course_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(headers1)):
            if i==0:
                continue
            course_view.setColumnWidth(i, 420)

        #设置课程详细的信息
        for row in range(len(res_info)//18):
            for col in range(len(headers2)):
                model_info.setItem(row,col,QStandardItem(res_info[row*len(headers2)+col]))
        course_view_info.setModel(model_info)
        course_view_info.setColumnWidth(2,352)
        # 设置列表只读
        course_view_info.setEditTriggers(QAbstractItemView.NoEditTriggers)
    #教学评估
    def teacher_assess(self):
        pass
    #获取学分绩点
    def get_group_point(self):
        thread =Gradepoint(self)
        def parse_grade_point(grade_point_value,grade_point_res, start_or_end_academic_term_res,academic_term_dic):
        #grade_point_value,grade_point_res, start_or_end_academic_term_res,academic_term_dic=APITool.Check_Group_Point()
            grade_point_model=QStandardItemModel(self.group_point_view)
            grade_headrs=["学年学期","学分绩"]
            grade_point_model.setColumnCount(len(grade_headrs))
            for idx, title in enumerate(grade_headrs):#设置数据头
                grade_point_model.setHeaderData(idx, Qt.Horizontal, title)
            #设置每个学期学分绩点
            for row in range(len(grade_point_res)//2):
                for col in range(len(grade_headrs)):
                    grade_point_model.setItem(row,col,QStandardItem(grade_point_res[row*len(grade_headrs)+col]))
            self.group_point_view.setModel(grade_point_model)
            self.group_point_view.setColumnWidth(0,235)#设置0列的宽度
            self.group_point_view.setColumnWidth(1,151)

            #获取平均的学分绩点
            self.grade_point_led.setText(grade_point_value)

            #添加下拉框信息
            self.start_cmbox.addItems(start_or_end_academic_term_res)
            self.end_cmbox.addItems(start_or_end_academic_term_res)

            flag=1
            if flag==1:
                self.loading_lab.hide()
        thread.rep_res_signal.connect(parse_grade_point)
        thread.start()  # 开始执行子线程任务
    #查询指定时间的绩点
    def query_fixed_timer_grade_point(self):
        #thread=FixedTimerGradepoint(self)#查询指定时间的绩点子线程
        academic_term_dic =APITool.Check_Group_Point()[3]
        if self.start_cmbox.currentText()!='--请选择--' and self.end_cmbox.currentText()!='--请选择--':
            start_timer=academic_term_dic[self.start_cmbox.currentText()]
            end_timer=academic_term_dic[self.end_cmbox.currentText()]
            print(end_timer[-3:-2],start_timer[-3:-2])
            if (int(end_timer[:4])> int(start_timer[:4])) or (int(end_timer[:4])== int(start_timer[:4]) and int(end_timer[-3:-2])>int(start_timer[-3:-2])):
                res=APITool.query_fixed_timer_Group_Point(start_timer,end_timer)
            else:
                end_timer=start_timer
                curr_index=self.start_cmbox.currentIndex()
                self.end_cmbox.Main_Page(curr_index)
                res=APITool.query_fixed_timer_Group_Point(start_timer,end_timer)
            self.group_point_lne.setText(res)
            return True
        return False
        #thread .rep_res_signal.connect(parse_Fixed_timer_grade_point)
        #thread.start()#开始执行子线程
    #设置视图和标签的样式
    def set_view_and_label_style(self,view,label1,label2=None):
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont("方正粗黑宋简体"))
        label1.setStyleSheet("QLabel{font:26px;}")

        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont("方正粗黑宋简体"))
        label2.setStyleSheet("QLabel{font:13px;}")

        view.setStyleSheet("QTableView QTableCornerButton::section {color: white;background-color: rgb(41, 139, 201);border: 5px solid #418bc9;border-radius:0px;border-color: rgb(41, 139, 201);font: 10px;"
                           "padding:0px 0 0 0px;}QHeaderView {color: white;font: bold 10pt;background-color: rgb(41, 139, 201);border: 0px solid rgb(144, 144, 144);border:0px solid rgb(191,191,191);border - left - color: "
                           "rgba(255, 255, 255, 0);border - top - color: rgba(255, 255, 255, 0);border-radius:0px;min-height:29px;}QHeaderView::section {color: white;background-color:rgb(41, 139, 201);"
                           "border: 5px solid #f6f7fa;border-radius:0px;border-color:rgb(41, 139, 201);}")
        view.verticalHeader().setVisible(False)
        view.setColumnWidth(0, 85)
        view.setColumnWidth(1, 62)
        view.setColumnWidth(2, 175)
        view.setColumnWidth(3, 135)
        view.setColumnWidth(4, 57)
        view.setColumnWidth(5, 86)
        view.setColumnWidth(6, 69)
    #设置表格
    def set_tableview(self,tableview,grade_info_list):
        grade_headrs = ["课程号", "课序号", "课程名", "英文课程名", "学分", "课程属性", "成绩"]
        grade_model = QStandardItemModel(tableview)
        grade_model.setColumnCount(len(grade_headrs))  # 设置列数
        for idx, title in enumerate(grade_headrs):  # 设置数据头
            grade_model.setHeaderData(idx, Qt.Horizontal, title)
        if len(grade_info_list)!=0:
            for row in range(len(grade_info_list) // 7):  # 设置成绩的详细数据
                for col in range(len(grade_headrs)):
                    grade_model.setItem(row, col, QStandardItem(grade_info_list[row * len(grade_headrs) + col]))
            tableview.setModel(grade_model)
    # 查询全部及格成绩
    def all_pass_grade(self):
        school_year_list, grade_info_list=APITool.query_pass_grade()
        self.set_tableview(self.allgarde_vie,grade_info_list)
        self.garde_timer_lab.setText(school_year_list[0]+"------"+school_year_list[-1])#设置成绩的学期详细时间
        #设置列表视图的列宽
        self.allgarde_vie.setColumnWidth(0, 97)
        self.allgarde_vie.setColumnWidth(1, 65)
        self.allgarde_vie.setColumnWidth(2, 145)
        self.allgarde_vie.setColumnWidth(3, 157)
        self.allgarde_vie.setColumnWidth(4, 50)
        self.allgarde_vie.setColumnWidth(5, 79)
        self.allgarde_vie.setColumnWidth(6, 55)
    #设置不及格成绩的表格视图
    def set_nopass_view(self,tableview,label,data_key,data_list):
        label.setText(data_key)
        grade_headrs = ["课程号", "课序号", "课程名", "英文课程名", "学分", "课程属性", "成绩","考试时间","特殊原因"]
        grade_model = QStandardItemModel(tableview)
        grade_model.setColumnCount(len(grade_headrs))  # 设置列数
        for idx, title in enumerate(grade_headrs):  # 设置数据头
            grade_model.setHeaderData(idx, Qt.Horizontal, title)
        if len(data_list) != 0:
            for row in range(len(data_list) // 9):  # 设置成绩的详细数据
                for col in range(len(grade_headrs)):
                    grade_model.setItem(row, col, QStandardItem(data_list[row * len(grade_headrs) + col]))
            tableview.setModel(grade_model)
    #查询全部不及格成绩
    def all_nopass_grade(self):
        nopass_dic, nopass_lab_dic=APITool.get_no_pass_score()
        self.set_nopass_view(self.now_nopass_viw,self.now_nopass_lab,nopass_lab_dic["尚不及格"],nopass_dic["尚不及格"])
        self.set_nopass_view(self.old_nopass_viw, self.old_nopass_lab, nopass_lab_dic["曾不及格"],nopass_dic["曾不及格"])
    #设置每个学期的成绩
    def Set_each_semester_grade(self,tableview,label,res_dic):
        grade_headrs = ["课程号", "课序号", "课程名", "英文课程名", "学分", "课程属性", "成绩"]
        grade_model = QStandardItemModel(tableview)
        grade_model.setColumnCount(len(grade_headrs))  # 设置列数
        for idx, title in enumerate(grade_headrs):#添加数据头
            grade_model.setHeaderData(idx, Qt.Horizontal, title)
        for key,value in res_dic.items():
            if label.text()==key:
                for row in range(len(value) // 7):  # 设置成绩的详细数据
                    for col in range(len(grade_headrs)):
                        grade_model.setItem(row, col, QStandardItem(value[row * len(grade_headrs) + col]))
        tableview.setModel(grade_model)
    #获取本学期的成绩信息
    def get_this_semester_info(self):
        this_semester_score_list=APITool.get_this_semester_score()
        #设置表格数据
        headrs = ["课程号", "课序号", "课程名", "英文课程名", "学分", "课程属性", "课堂最高分", "课堂最低分", "课堂平均分", "成绩", "名次", "未通过原因", "明细"]
        model = QStandardItemModel(self.this_semester_view)
        model.setColumnCount(len(headrs))  # 设置列数
        for idx, title in enumerate(headrs):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for row in range(len(this_semester_score_list) // len(headrs)):  # 设置成绩的详细数据
            for col in range(len(headrs)):
                model.setItem(row, col, QStandardItem(this_semester_score_list[row * len(headrs) + col]))
        self.this_semester_view.setModel(model)
        self.this_semester_view.setColumnWidth(2,153)
    #设置表格和标签数据
    def set_tableview_label_data(self,tableview,label,data_key,data_list):
        label.setText(data_key)
        self.set_tableview(tableview,data_list)
        tableview.setColumnWidth(0, 95)
        tableview.setColumnWidth(1, 76)
        tableview.setColumnWidth(2, 182)
        tableview.setColumnWidth(3, 323)
        tableview.setColumnWidth(4, 68)
        tableview.setColumnWidth(5, 89)
        tableview.setColumnWidth(6, 75)
    #设置课程属性成绩
    def set_course_attribute_score(self):
        grade_attribute_dic, course_info_dic=APITool.get_course_attribute_score()
        if '必修' in grade_attribute_dic.keys():
            self.set_tableview_label_data(self.Compulsory_view,self.Compulsory_info_lab,course_info_dic["必修"],grade_attribute_dic["必修"])
        else:
            self.Compulsory_info_lab.setText("您当前并没有必修课程")
        if '选修' in grade_attribute_dic.keys():
            self.set_tableview_label_data(self.Elective_view, self.Elective_info_lab, course_info_dic["选修"],grade_attribute_dic["选修"])
        else:
            self.Elective_info_lab.setText("您当前并没有选修课程")
        if '任选' in grade_attribute_dic.keys():
            self.set_tableview_label_data(self.Pick_view, self.Pick_info_lab, course_info_dic["任选"],grade_attribute_dic["任选"])
        else:
            self.Pick_info_lab.setText("您当前并没有任选课程")
    #设置方案成绩
    def set_plan_score(self):
        title_info, take_credits_info, group_info, tail_info,course_info_list=APITool.get_plan_socre()
        self.title_label.setText(title_info)
        self.plan_score_info_lab.setText(take_credits_info)
        self.plan_groupBox.setTitle(group_info)
        self.plan_info_lab.setText(tail_info)
        self.set_tableview(self.plan_score_view,course_info_list)
        #设置表格的列宽
        self.plan_score_view.setColumnWidth(0, 104)
        self.plan_score_view.setColumnWidth(1, 68)
        self.plan_score_view.setColumnWidth(2, 182)
        self.plan_score_view.setColumnWidth(3, 304)
        self.plan_score_view.setColumnWidth(4, 71)
        self.plan_score_view.setColumnWidth(5, 97)
        self.plan_score_view.setColumnWidth(6, 69)
    #动态设置列表和表格视图数据
    def list_and_view_date(self):
        #首先清空防止重复添加数据
        self.scool_year_lwid.clear()
        self.scool_year_lwid.addItem("全部学期的及格成绩")
        school_year_list, grade_info_list = APITool.query_pass_grade()
        self.scool_year_lwid.addItems(school_year_list)#添加数据
        self.scool_year_lwid.setCurrentRow(0)#设置默认为第0项
        self.flag=True#标识为真,表示已经创建过一次
        #创建动态的Widget(随着学期数量)
        if self.flag:
            res_dic,minimum_credit_list=APITool.Get_semester_data()#获取每个学期对应的成绩和最低修读学分等信息
            for count in range(len(school_year_list)):
                #动态创建LISTVIEW和label 来添加每个学期的及格成绩
                layout= QVBoxLayout()
                title=QLabel(school_year_list[count],self)
                tail=QLabel(minimum_credit_list[count],self)
                new_Tableview=QTableView(self)
                self.Set_each_semester_grade(new_Tableview,title,res_dic)#设置信息到表格和标签上
                self.set_view_and_label_style(new_Tableview, title, tail)  # 设置样式
                widget = QWidget(self)
                layout.addWidget(title)
                layout.addWidget(new_Tableview)
                layout.addWidget(tail)
                widget.setLayout(layout)
                self.stackedWidget.addWidget(widget)
    #ListWidget改变行触发QStackedWidget切换的槽函数
    def setCurrentIndex(self,index):
        print("我发生了改变")
    #设置综合查询的课程基本信息页面
    def set_course_info_page(self):
        department_info_dic, course_category_dic, page_num_res=APITool.get_course_department_and_category_info()
        self.Department_cob.clear()#首先清空下拉列表,防止重复添加
        self.category_cob.clear()

        #设置相应的数据到下拉列表内
        self.Department_cob.addItems(department_info_dic.keys())
        self.category_cob.addItems(course_category_dic.keys())

        #设置对应的初始值
        self.course_info_lab.setText(page_num_res)
        self.firstpage_btn.setEnabled(False)
        self.Previous_btn.setEnabled(False)
        self.next_btn.setEnabled(False)
        self.endpage_btn.setEnabled(False)
        self.page_cob.setEnabled(False)
    #更新综合查询页面的课程基本信息表格视图
    def updata_query_course_view(self,tableview,res_list):
        headrs = ["序号", "课程号", "课程名", "开课院系", "课程类别", "查看"]
        model = QStandardItemModel(tableview)
        model.setColumnCount(len(headrs))  # 设置列数
        for idx, title in enumerate(headrs):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for row in range(len(res_list) // len(headrs)):  # 设置成绩的详细数据
            for col in range(len(headrs)):
                model.setItem(row, col, QStandardItem(res_list[row * len(headrs) + col]))
        tableview.setModel(model)
        tableview.setColumnWidth(2, 189)
        tableview.setColumnWidth(3, 150)
        tableview.setColumnWidth(4, 151)
        tableview.setColumnWidth(5, 148)
    #综合查询的课程基本信息的查询按钮槽函数
    def course_query(self):
        department_info_dic, course_category_dic, page_num_res = APITool.get_course_department_and_category_info()
        #传递相应的参数
        kkxsh=department_info_dic[self.Department_cob.currentText()]
        kclbdm=course_category_dic[self.category_cob.currentText()]
        kch=self.Course_num_led.text()
        kcm=self.course_name_led.text()
        pageSize=self.page_cob.currentText()[:-1]

        page=page_num_res[page_num_res.index('第')+1]
        currentPage=page
        #获取请求的结果
        res_list, current_page=APITool.query_course_info(kkxsh,kclbdm,kch,kcm,pageSize,page,currentPage)
        #更新当前状态
        self.course_info_lab.setText(current_page)
        self.currentPage = currentPage  # 储存当前页数
        self.endPage=re.findall(".*/(.*)页.*",current_page)#结尾页数
        self.currentItem = re.findall(".*共(.*)项.*", current_page)#存储当前一共有多少项
        if re.findall(".*/(.*)页.*",current_page)=="0":
            return None
        self.next_btn.setEnabled(True)
        self.endpage_btn.setEnabled(True)
        self.page_cob.setEnabled(True)
        #更新显示列表视图
        self.updata_query_course_view(self.select_course_viw,res_list)
    # 综合查询的课程基本信息的下拉框槽函数
    def set_view_page_num(self,qstr):
        page=self.currentPage #更新当前页数
        res_list, current_page = APITool.new_course_info(self.currentItem, page, qstr[:-1])
        self.updata_query_course_view(self.select_course_viw, res_list)  # 更新视图
        self.course_info_lab.setText(current_page)  # 更新标签信息
    #综合查询的课程基本信息的首页按钮槽函数
    def return_firstpage(self):
        page = str(1)
        self.currentPage = page  # 更新当前页数
        res_list, current_page = APITool.new_course_info(self.currentItem, page, self.page_cob.currentText()[:-1])
        self.updata_query_course_view(self.select_course_viw, res_list)  # 更新视图
        self.course_info_lab.setText(current_page)  # 更新标签信息
        self.firstpage_btn.setEnabled(False)
        self.Previous_btn.setEnabled(False)
        self.next_btn.setEnabled(True)
        self.endpage_btn.setEnabled(True)
    # 综合查询的课程基本信息的末页按钮槽函数
    def return_endpage(self):
        page=str(int(self.endPage[0]))
        self.currentPage=page# 更新当前页数
        res_list, current_page = APITool.new_course_info(self.currentItem, page, self.page_cob.currentText()[:-1])
        self.updata_query_course_view(self.select_course_viw, res_list)  # 更新视图
        self.course_info_lab.setText(current_page)  # 更新标签信息
        self.firstpage_btn.setEnabled(True)
        self.Previous_btn.setEnabled(True)
        self.next_btn.setEnabled(False)
        self.endpage_btn.setEnabled(False)
    # 综合查询的课程基本信息的上一页按钮槽函数
    def ret_front_page(self):
        page = str(int(self.currentPage) - 1)
        self.currentPage = page  # 更新当前页数
        res_list, current_page = APITool.new_course_info(self.currentItem, page, self.page_cob.currentText()[:-1])
        self.updata_query_course_view(self.select_course_viw, res_list)  # 更新视图
        self.course_info_lab.setText(current_page)  # 更新标签信息
        if int(self.currentPage)==1:
            self.firstpage_btn.setEnabled(False)
            self.Previous_btn.setEnabled(False)
            self.next_btn.setEnabled(True)
            self.endpage_btn.setEnabled(True)
        else:
            self.firstpage_btn.setEnabled(True)
            self.Previous_btn.setEnabled(True)
            self.next_btn.setEnabled(True)
            self.endpage_btn.setEnabled(True)
    # 综合查询的课程基本信息的下一页按钮槽函数
    def ret_next_page(self):
        page=str(int(self.currentPage)+1)
        self.currentPage=page#更新当前页数
        res_list, current_page=APITool.new_course_info(self.currentItem,page,self.page_cob.currentText()[:-1])
        self.updata_query_course_view(self.select_course_viw, res_list)#更新视图
        self.course_info_lab.setText(current_page)#更新标签信息
        if int(self.currentPage)==int(self.endPage[0]):
            self.firstpage_btn.setEnabled(True)
            self.Previous_btn.setEnabled(True)
            self.next_btn.setEnabled(False)
            self.endpage_btn.setEnabled(False)
        else:
            self.firstpage_btn.setEnabled(True)
            self.Previous_btn.setEnabled(True)
            self.next_btn.setEnabled(True)
            self.endpage_btn.setEnabled(True)
    #初始化本学期课程安排表格视图
    def Init_list_view(self,headers,tableview,res_list,label,label_text):
        label.setText(label_text)
        model = QStandardItemModel(tableview)
        model.setColumnCount(len(headers))  # 设置列数
        for idx, title in enumerate(headers):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for row in range(len(res_list) // len(headers)):  # 设置成绩的详细数据
            for col in range(len(headers)):
                model.setItem(row, col, QStandardItem(res_list[row * len(headers) + col]))
        tableview.setModel(model)
    #本学期课程安排初始化信息
    def Init_course_arrange(self):
        Department_dic, class_week_dic, class_num_dic, show_col_dic,token=APITool.semester_course_arrange()

        #清空控件防止重复添加数据
        self.Department2_cob.clear()
        self.week_cob.clear()
        self.class_num_cob.clear()
        self.show_item_list_widget.clear()

        #初始化控件
        self.Department2_cob.addItems(Department_dic.keys())
        self.week_cob.addItems(class_week_dic.keys())
        self.class_num_cob.addItems(class_num_dic.keys())
        self.show_item_list_widget.addItems(show_col_dic.keys())

        #隐藏相应的按钮
        self.Previous2_btn.setEnabled(False)
        self.next2_btn.setEnabled(False)
    #本学期课程安排查询按钮槽函数
    def query_course_arrange_info(self):
        Department_dic, class_week_dic, class_num_dic, show_col_dic, token = APITool.semester_course_arrange()
        course_num=self.course_number_led.text()
        course_name=self.course_name2_led.text()
        teach_name=self.teach_led.text()
        Department=Department_dic[self.Department2_cob.currentText()]
        week=class_week_dic[self.week_cob.currentText()]
        class_num=class_num_dic[self.class_num_cob.currentText()]
        Campus=self.Campus_cob.currentIndex()
        Campus_num=""#校区编号
        if str(Campus)!="0":
            Campus_num="0"+str(Campus)
        show_num=self.page_number_cob.currentText()[:-1]
        show_col_list=[]
        for key in show_col_dic:
            show_col_list.append(show_col_dic[key])
        pageNumber=str(self.show_item_list_widget.currentIndex())
        headrs, course_info_list, page_num=APITool.course_arrange_info_data(token,course_num,course_name,teach_name,Department,week,class_num,Campus_num,show_num,show_col_list,pageNumber)
        self.page2_led.setText(show_num)
        self.Init_list_view(headrs,self.tableView ,course_info_list,self.course_info2_lab ,page_num)
        self.current_page = re.findall(".*第(.*)页.*", page_num)[0]#保存当前页数
        self.next2_btn.setEnabled(True)
    #本学期课程安排 上一页
    def ret_firstpage(self):
        self.current_page = int(self.current_page) - 1
        current_page = str(self.current_page)
        headrs, course_info_list, page_num = APITool.Process_Page_turning(current_page)
        self.Init_list_view(headrs, self.tableView, course_info_list, self.course_info2_lab, page_num)
        if str(self.current_page)=="1":
            self.Previous2_btn.setEnabled(False)
    # 本学期课程安排 下一页
    def ret_endpage(self):
        self.current_page=int(self.current_page)+1
        current_page=str(self.current_page)
        headrs, course_info_list, page_num=APITool.Process_Page_turning(current_page)
        self.Init_list_view(headrs, self.tableView, course_info_list, self.course_info2_lab, page_num)
        self.Previous2_btn.setEnabled(True)
        if str(self.current_page)==re.findall(".*共(.*)页.*", page_num)[0]:
            self.next2_btn.setEnabled(False)
    #在表格中设置按钮
    def In_the_view_btn(self,view,pageSize,col1,string="查看"):
        for idx in range(int(pageSize)):
            m_button=QPushButton(self)
            m_button.setText(string)
            model=view.model()
            view.setIndexWidget(model.index(idx,col1),m_button)
    #初始化教室课表
    def Init_Classroom_Schedule_info(self):
        Academic_term_dic, Campus_dic=APITool.Classroom_Schedule_info_data()

        #初始化控件
        self.classroom_Academic_term_cob.clear()#防止重复添加数据 先清空
        self.classroom_Campus_cob.clear()#同上
        self.classroom_Teaching_building_cob.clear()
        self.classroom_class_cob.clear()
        self.Previous_btn_2.setEnabled(False)
        self.classroom_firstpage_btn.setEnabled(False)
        self.classroom_next_btn.setEnabled(False)
        self.classroom_endpage_btn.setEnabled(False)

        #添加数据
        self.classroom_Academic_term_cob.addItems(Academic_term_dic.keys())
        self.classroom_Academic_term_cob.setCurrentIndex(len(Academic_term_dic)-1)
        self.classroom_Campus_cob.addItems(Campus_dic.keys())
        Init_list=["请选择"]
        self.classroom_Teaching_building_cob.addItems(Init_list)
        self.classroom_class_cob.addItems(Init_list)
    #教室课表中，选择校区后显示教学楼槽函数。
    def show_teaching_building(self,index):
        if index==0 or index==-1:
            return None
        Academic_term_dic, Campus_dic = APITool.Classroom_Schedule_info_data()
        self.classroom_Teaching_building_cob.clear()
        js_zxjxjhh=Academic_term_dic[self.classroom_Academic_term_cob.currentText()]
        js_xq=Campus_dic[self.classroom_Campus_cob.currentText()]
        pageSize=self.classroom_page_cob.currentText()[:-1]
        Teaching_building_dic=APITool.get_Teaching_building_data(js_zxjxjhh,js_xq,pageSize)
        self.classroom_Teaching_building_cob.addItems(Teaching_building_dic.keys())

    #教室课表中，选择教学楼后显示教室
    def show_classroom(self,index):
        if index==0 or index==-1:
            return None
        Academic_term_dic, Campus_dic = APITool.Classroom_Schedule_info_data()
        #self.classroom_Teaching_building_cob.clear()
        self.classroom_class_cob.clear()

        js_zxjxjhh = Academic_term_dic[self.classroom_Academic_term_cob.currentText()]
        js_xq = Campus_dic[self.classroom_Campus_cob.currentText()]
        pageSize = self.classroom_page_cob.currentText()[:-1]
        Teaching_building_dic=APITool.get_Teaching_building_data(js_zxjxjhh,js_xq,pageSize)
        js_jxl=Teaching_building_dic[self.classroom_Teaching_building_cob.currentText()]

        res = APITool.get_classroom_info(js_zxjxjhh, js_xq, pageSize,js_jxl)
        self.classroom_class_cob.addItems(res.keys())
    #教室课表信息查询槽函数
    def query_classroom_curriculum(self):
        #获取对应控件的值
        Academic_term_dic, Campus_dic = APITool.Classroom_Schedule_info_data()
        js_zxjxjhh = Academic_term_dic[self.classroom_Academic_term_cob.currentText()]
        js_xq = Campus_dic[self.classroom_Campus_cob.currentText()]
        pageSize = self.classroom_page_cob.currentText()[:-1]
        Teaching_building_dic = APITool.get_Teaching_building_data(js_zxjxjhh, js_xq, pageSize)
        js_jxl = Teaching_building_dic[self.classroom_Teaching_building_cob.currentText()]
        classroom_dic = APITool.get_classroom_info(js_zxjxjhh, js_xq, pageSize, js_jxl)
        js_js=classroom_dic[self.classroom_class_cob.currentText()]

        #获取请求结果
        headrs, classroom_info_list, page_num=APITool.query_classroom_curriculum_info(js_zxjxjhh,js_xq,pageSize,js_jxl,js_js)
        #设置视图显示
        self.Init_list_view(headrs,self.classroom_view,classroom_info_list,self.classroom_course_info_lab,page_num)
        #设置控件
        self.classroom_firstpage_btn.setEnabled(False)
        self.Previous_btn_2.setEnabled(False)
        self.classroom_next_btn.setEnabled(True)
        self.classroom_endpage_btn.setEnabled(True)
        #设置当前页数
        self.classroom_page=1
        #获取总页数
        total_Page = re.findall(".*/(.*)页.*", self.classroom_course_info_lab.text())[0]  # 总页数
        if total_Page=="1" or total_Page=="0":
            self.classroom_next_btn.setEnabled(True)
            self.classroom_endpage_btn.setEnabled(True)
        self.In_the_view_btn(self.classroom_view,pageSize,8)
        self.In_the_view_btn(self.classroom_view,pageSize, 9)
    #教室课表信息上一页
    def ret_classroom_curriculum_Previous(self):
        self.classroom_page =int(self.classroom_page)-1  # 当前页数
        page = self.classroom_page
        PageSize = self.classroom_page_cob.currentText()[:-1]  # 显示数据的项数
        total_rows = re.findall(".*共(.*)项.*", self.classroom_course_info_lab.text())[0]  # 总项数
        total_Page = re.findall(".*/(.*)页.*", self.classroom_course_info_lab.text())[0]  # 总页数
        headrs, info_list, page_num = APITool.replace_classroom_page(total_rows, str(page), PageSize)

        # 设置控件
        if total_Page == "0" or page==1:
            self.Previous_btn_2.setEnabled(False)
            self.classroom_firstpage_btn.setEnabled(False)
        self.classroom_next_btn.setEnabled(True)
        self.classroom_endpage_btn.setEnabled(True)
        # 设置视图显示
        self.Init_list_view(headrs, self.classroom_view, info_list, self.classroom_course_info_lab, page_num)
        self.In_the_view_btn(self.classroom_view, PageSize, 8)
        self.In_the_view_btn(self.classroom_view, PageSize, 9)
    #教室课表信息下一页
    def ret_classroom_curriculum_next(self):
        #获取数据和发送请求
        self.classroom_page+=1#当前页数
        page=self.classroom_page
        PageSize=self.classroom_page_cob.currentText()[:-1]#显示数据的项数
        total_rows=re.findall(".*共(.*)项.*",self.classroom_course_info_lab.text())[0]#总项数
        total_Page=re.findall(".*/(.*)页.*",self.classroom_course_info_lab.text())[0]#总页数
        headrs, info_list, page_num=APITool.replace_classroom_page(total_rows,str(page),PageSize)

        #设置控件
        if total_Page ==str(page):
            self.classroom_next_btn.setEnabled(False)
            self.classroom_endpage_btn.setEnabled(False)
        self.Previous_btn_2.setEnabled(True)
        self.classroom_firstpage_btn.setEnabled(True)
        # 设置视图显示
        self.Init_list_view(headrs, self.classroom_view, info_list, self.classroom_course_info_lab, page_num)
        self.In_the_view_btn(self.classroom_view, PageSize, 8)
        self.In_the_view_btn(self.classroom_view, PageSize, 9)
    #教室课表信息首页
    def ret_classroom_curriculum_first(self):
        # 获取数据和发送请求
        self.classroom_page=1
        page=self.classroom_page
        PageSize = self.classroom_page_cob.currentText()[:-1]  # 显示数据的项数
        total_rows = re.findall(".*共(.*)项.*", self.classroom_course_info_lab.text())[0]  # 总项数
        headrs, info_list, page_num = APITool.replace_classroom_page(total_rows, str(page), PageSize)

        #设置控件
        self.Previous_btn_2.setEnabled(False)
        self.classroom_firstpage_btn.setEnabled(False)
        self.classroom_next_btn.setEnabled(True)
        self.classroom_endpage_btn.setEnabled(True)
        # 设置视图显示
        self.Init_list_view(headrs, self.classroom_view, info_list, self.classroom_course_info_lab, page_num)
        self.In_the_view_btn(self.classroom_view, PageSize, 8)
        self.In_the_view_btn(self.classroom_view, PageSize, 9)
    #教室课表信息尾页
    def ret_classroom_curriculum_end(self):
        # 获取数据和发送请求
        total_Page = re.findall(".*/(.*)页.*", self.classroom_course_info_lab.text())[0]#总页数
        print(total_Page)
        self.classroom_page=total_Page
        page=self.classroom_page
        print(page)
        PageSize = self.classroom_page_cob.currentText()[:-1]  # 显示数据的项数
        total_rows = re.findall(".*共(.*)项.*", self.classroom_course_info_lab.text())[0]  # 总项数

        headrs, info_list, page_num = APITool.replace_classroom_page(total_rows, str(page), PageSize)

        # 设置控件
        self.Previous_btn_2.setEnabled(True)
        self.classroom_firstpage_btn.setEnabled(True)
        self.classroom_next_btn.setEnabled(False)
        self.classroom_endpage_btn.setEnabled(False)
        # 设置视图显示
        self.Init_list_view(headrs, self.classroom_view, info_list, self.classroom_course_info_lab, page_num)
        self.In_the_view_btn(self.classroom_view, PageSize, 8)
        self.In_the_view_btn(self.classroom_view, PageSize, 9)
    # 初始化教师课表信息
    def Init_teacher_curriculum_info(self):
        teacher_Init_info_dic, Department_info_dic = APITool.get_teacher_Basicinfo()#获取学年和院系信息
        self.teach_Academic_term_cob.clear()#先清空防止重复添加
        self.teach_Department_cob.clear()

        #设置下拉框
        self.teach_Academic_term_cob.addItems(teacher_Init_info_dic.keys())
        self.teach_Academic_term_cob.setCurrentIndex(len(teacher_Init_info_dic)-3)
        self.teach_Department_cob.addItems(Department_info_dic.keys())

        #初始化控件
        self.teach_firstpage_btn.setEnabled(False)
        self.teach_Previous_btn.setEnabled(False)
        self.teach_next_btn.setEnabled(False)
        self.teach_endpage_btn.setEnabled(False)
    #查询教师信息按钮
    def query_teacher_info(self):
        self.current_page=1#设置当前页数
        teacher_Init_info_dic, Department_info_dic = APITool.get_teacher_Basicinfo()  # 获取学年和院系信息
        #获取数据和教学详细信息
        lsxnxq=teacher_Init_info_dic[self.teach_Academic_term_cob.currentText()]
        lsxsh=Department_info_dic[self.teach_Department_cob.currentText()]
        lsjsm=self.teach_name_led.text()
        pageSize=self.teach_page_cob.currentText()[:-1]
        headrs, info_list, page_num=APITool.get_teacher_detailedinfo(lsxnxq,lsxsh,lsjsm,pageSize)#获取数据
        self.Init_list_view(headrs, self.teach_view, info_list, self.teach_course_info_lab, page_num)
        #设置表格列宽
        self.teach_view.setColumnWidth(2, 221)
        self.teach_view.setColumnWidth(3, 256)
        self.teach_view.setColumnWidth(4, 156)
        #设置显示按钮
        total_page = re.findall(".*/(.*)页.*", self.teach_course_info_lab.text())[0] #总页数
        if total_page!="1":
            self.teach_next_btn.setEnabled(True)
            self.teach_endpage_btn.setEnabled(True)
    #教师课表首页按钮
    def ret_teacher_first(self):
        totalrows = re.findall(".*共(.*)项.*", self.teach_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.teach_course_info_lab.text())[0]  # 总页数
        self.current_page = 1
        page = str(self.current_page)
        pageSize = self.teach_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_teacherPage_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.teach_view, info_list, self.teach_course_info_lab, page_num)
        # 设置表格列宽
        self.teach_view.setColumnWidth(2, 211)
        self.teach_view.setColumnWidth(3, 256)
        self.teach_view.setColumnWidth(4, 156)

        # 设置控件显示
        self.teach_firstpage_btn.setEnabled(False)
        self.teach_Previous_btn.setEnabled(False)
        self.teach_next_btn.setEnabled(True)
        self.teach_endpage_btn.setEnabled(True)
        if totalpage=="1" or totalpage=="0":
            self.teach_next_btn.setEnabled(False)
            self.teach_endpage_btn.setEnabled(False)
    #教师课表上一页按钮
    def ret_teacher_Previous(self):
        self.current_page = self.current_page - 1
        totalrows = re.findall(".*共(.*)项.*", self.teach_course_info_lab.text())[0]  # 总项数
        page = str(self.current_page)
        pageSize = self.teach_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_teacherPage_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.teach_view, info_list, self.teach_course_info_lab, page_num)
        # 设置表格列宽
        self.teach_view.setColumnWidth(2, 211)
        self.teach_view.setColumnWidth(3, 256)
        self.teach_view.setColumnWidth(4, 156)
        # 设置显示按钮
        self.teach_next_btn.setEnabled(True)
        self.teach_endpage_btn.setEnabled(True)
        if page == "1":
            self.teach_firstpage_btn.setEnabled(False)
            self.teach_Previous_btn.setEnabled(False)
    #教师课表下一页按钮
    def ret_teacher_Next(self):
        self.current_page=self.current_page+1
        totalrows=re.findall(".*共(.*)项.*", self.teach_course_info_lab.text())[0]  # 总项数
        totalpage=re.findall(".*/(.*)页.*", self.teach_course_info_lab.text())[0]  # 总页数
        page=str(self.current_page)
        pageSize=self.teach_page_cob.currentText()[:-1]
        headrs, info_list, page_num=APITool.get_replace_teacherPage_info(totalrows,page,pageSize)
        self.Init_list_view(headrs, self.teach_view, info_list, self.teach_course_info_lab, page_num)
        # 设置表格列宽
        self.teach_view.setColumnWidth(2, 211)
        self.teach_view.setColumnWidth(3, 256)
        self.teach_view.setColumnWidth(4, 156)
        #设置显示按钮
        self.teach_firstpage_btn.setEnabled(True)
        self.teach_Previous_btn.setEnabled(True)
        if page==totalpage:
            self.teach_next_btn.setEnabled(False)
            self.teach_endpage_btn.setEnabled(False)
    #教师课表尾页按钮
    def ret_teacher_end(self):
        #传递以及获取对应的数据
        totalrows = re.findall(".*共(.*)项.*", self.teach_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.teach_course_info_lab.text())[0]  # 总页数
        self.current_page = int(totalpage)
        page = str(self.current_page)
        pageSize = self.teach_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_teacherPage_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.teach_view, info_list, self.teach_course_info_lab, page_num)
        # 设置表格列宽
        self.teach_view.setColumnWidth(2, 211)
        self.teach_view.setColumnWidth(3, 256)
        self.teach_view.setColumnWidth(4, 156)

        #设置控件显示
        self.teach_firstpage_btn.setEnabled(True)
        self.teach_Previous_btn.setEnabled(True)
        self.teach_next_btn.setEnabled(False)
        self.teach_endpage_btn.setEnabled(False)

    #初始化课程课表
    def Init_course_curriculum_info(self):
        Academic_term_info_dic, Department_info_dic = APITool.get_teacher_Basicinfo() #获取学年和院系信息

        self.curriculum_Academic_term_cob.clear()#首先清空 防止重复添加
        self.curriculum_Department_cob.clear()

        #设置下拉框
        self.curriculum_Academic_term_cob.addItems(Academic_term_info_dic.keys())
        self.curriculum_Academic_term_cob.setCurrentIndex(len(Academic_term_info_dic) - 3)
        self.curriculum_Department_cob.addItems(Department_info_dic.keys())

        #设置控件显示
        self.curriculum_firstpage_btn.setEnabled(False)
        self.curriculum_Previous_btn.setEnabled(False)
        self.curriculum_next_btn.setEnabled(False)
        self.curriculum_endpage_btn.setEnabled(False)
    #查询课程课表信息按钮槽函数
    def query_course_curriculum_info(self):
        #初始化页数
        self.current_page=1
        Academic_term_info_dic, Department_info_dic = APITool.get_teacher_Basicinfo()  # 获取学年和院系信息
        #传递以及获取数据
        kcxnxq=Academic_term_info_dic[self.curriculum_Academic_term_cob.currentText()]
        kckcm=self.curriculum_course_name_led.text()
        xsh=Department_info_dic[self.curriculum_Department_cob.currentText()]
        kckch=self.curriculum_course_num_led.text()
        kckxh=self.curriculum_curse_order_led.text()
        pageSize=self.curriculum_page_cob.currentText()[:-1]
        headrs,info_list, page_num=APITool.get_course_detailedinfo(kcxnxq,kckcm,xsh,kckch,kckxh,pageSize)
        #设置视图
        self.Init_list_view(headrs, self.curriculum_view, info_list, self.curriculum_course_info_lab, page_num)
        self.In_the_view_btn(self.curriculum_view, pageSize, 8)
        #显示按钮
        totalpage = re.findall(".*/(.*)页.*", self.curriculum_course_info_lab.text())[0] #总页数
        self.curriculum_firstpage_btn.setEnabled(False)
        self.curriculum_Previous_btn.setEnabled(False)
        self.curriculum_next_btn.setEnabled(True)
        self.curriculum_endpage_btn.setEnabled(True)
        if totalpage=="1" or totalpage=="0":
            self.curriculum_next_btn.setEnabled(False)
            self.curriculum_endpage_btn.setEnabled(False)
    #课程课表返回首页
    def ret_course_first(self):
        totalrows = re.findall(".*共(.*)项.*", self.curriculum_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.curriculum_course_info_lab.text())[0]  # 总页数
        self.current_page = 1
        page = str(self.current_page)
        pageSize = self.curriculum_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_course_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.curriculum_view, info_list, self.curriculum_course_info_lab, page_num)
        self.In_the_view_btn(self.curriculum_view, pageSize, 8)

        # 设置控件显示
        self.curriculum_firstpage_btn.setEnabled(False)
        self.curriculum_Previous_btn.setEnabled(False)
        self.curriculum_next_btn.setEnabled(True)
        self.curriculum_endpage_btn.setEnabled(True)
        if totalpage == "1" or totalpage == "0":
            self.curriculum_next_btn.setEnabled(False)
            self.curriculum_endpage_btn.setEnabled(False)
    #课程课表上一页
    def ret_course_Previous(self):
        self.current_page = self.current_page - 1
        totalrows = re.findall(".*共(.*)项.*", self.curriculum_course_info_lab.text())[0]  # 总项数
        page = str(self.current_page)
        pageSize = self.curriculum_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_course_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.curriculum_view, info_list, self.curriculum_course_info_lab, page_num)
        self.In_the_view_btn(self.curriculum_view, pageSize, 8)
        self.curriculum_next_btn.setEnabled(True)
        self.curriculum_endpage_btn.setEnabled(True)
        if page=="1":
            self.curriculum_firstpage_btn.setEnabled(False)
            self.curriculum_Previous_btn.setEnabled(False)
    #课程课表下一页
    def ret_course_Next(self):
        self.current_page = self.current_page + 1
        totalrows = re.findall(".*共(.*)项.*", self.curriculum_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.curriculum_course_info_lab.text())[0]  # 总页数
        page = str(self.current_page)
        pageSize = self.curriculum_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_course_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.curriculum_view, info_list, self.curriculum_course_info_lab, page_num)
        self.In_the_view_btn(self.curriculum_view, pageSize, 8)
        # 设置显示按钮
        self.curriculum_firstpage_btn.setEnabled(True)
        self.curriculum_Previous_btn.setEnabled(True)
        print(totalpage)
        if page ==totalpage:
            self.curriculum_next_btn.setEnabled(False)
            self.curriculum_endpage_btn.setEnabled(False)
    #课程课表尾页
    def ret_course_End(self):
        # 传递以及获取对应的数据
        totalrows = re.findall(".*共(.*)项.*", self.curriculum_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.curriculum_course_info_lab.text())[0]  # 总页数
        self.current_page = int(totalpage)
        page = str(self.current_page)
        pageSize = self.curriculum_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_course_info(totalrows, page, pageSize)
        self.Init_list_view(headrs, self.curriculum_view, info_list, self.curriculum_course_info_lab, page_num)
        self.In_the_view_btn(self.curriculum_view, pageSize, 8)

        # 设置控件显示
        self.curriculum_firstpage_btn.setEnabled(True)
        self.curriculum_Previous_btn.setEnabled(True)
        self.curriculum_next_btn.setEnabled(False)
        self.curriculum_endpage_btn.setEnabled(False)
    #初始化班级课表
    def Init_class_curriculum_info(self):
        #获取初始化信息
        Academic_term_dic, Dept_dic, grade_dic=APITool.get_class_initinfo()

        #首先清空控件 防止重复添加
        self.Class_Academic_term_cob.clear()
        self.Class_Department_cob.clear()
        self.Class_grade_cob.clear()

        #设置控件
        self.Class_Academic_term_cob.addItems(Academic_term_dic.keys())
        self.Class_Academic_term_cob.setCurrentIndex(len(Academic_term_dic) - 3)
        self.Class_Department_cob.addItems(Dept_dic)
        self.Class_grade_cob.addItems(grade_dic)
    # 成绩查询页面
    #班级课表显示院系的专业信息
    def show_profession_info(self,index):
        if index==0 or index==-1:
            self.Class_profession_cob.clear()
            self.Class_profession_cob.addItems(["请选择"])
            return None
        Academic_term_dic, Dept_dic, grade_dic = APITool.get_class_initinfo()#获取初始化信息
        bjxnxq=Academic_term_dic[self.Class_Academic_term_cob.currentText()]#学期学年编号
        bjxsh=Dept_dic[self.Class_Department_cob.currentText()]#院系编号
        pageSize=self.Class_page_cob.currentText()[:-1]#显示项数
        profession_info_dic=APITool.get_grade_and_pro_info(bjxnxq,bjxsh,pageSize)

        self.Class_profession_cob.clear()#先清空再设置 防止重复添加
        #设置控件
        self.Class_profession_cob.addItems(profession_info_dic.keys())
    #班级课表显示年级的班级信息
    def show_class_info(self,index):
        if index==0 or index==-1:
            self.Class_class_cob.clear()
            self.Class_class_cob.addItems(["请选择"])
            return None
        Academic_term_dic, Dept_dic, grade_dic = APITool.get_class_initinfo()  # 获取初始化信息
        bjxnxq = Academic_term_dic[self.Class_Academic_term_cob.currentText()]  # 学期学年编号
        bjxsh=Dept_dic[self.Class_Department_cob.currentText()]#院系编号
        nj = grade_dic[self.Class_grade_cob.currentText()] #年级编号
        pageSize = self.Class_page_cob.currentText()[:-1]  # 显示项数
        profession_info_dic = APITool.get_grade_and_pro_info(bjxnxq, bjxsh, pageSize)
        bjzyh=profession_info_dic[self.Class_profession_cob.currentText()]#专业编号
        class_info_dic = APITool.get_class_info(bjxnxq,bjxsh,bjzyh, nj, pageSize)

        self.Class_class_cob.clear()  # 先清空再设置 防止重复添加
        # 设置控件
        self.Class_class_cob.addItems(class_info_dic.keys())
    #查询班级信息槽函数
    def query_class_info(self):
        self.current_page=1#初始化页数
        #获取班级信息
        Academic_term_dic, Dept_dic, grade_dic = APITool.get_class_initinfo()  # 获取初始化信息
        bjxnxq = Academic_term_dic[self.Class_Academic_term_cob.currentText()]  # 学期学年编号
        bjxsh = Dept_dic[self.Class_Department_cob.currentText()]  # 院系编号
        nj = grade_dic[self.Class_grade_cob.currentText()]  # 年级编号
        pageSize = self.Class_page_cob.currentText()[:-1]  # 显示项数
        profession_info_dic = APITool.get_grade_and_pro_info(bjxnxq, bjxsh, pageSize)#获取专业请求
        bjzyh = profession_info_dic[self.Class_profession_cob.currentText()]  # 专业编号
        class_info_dic=APITool.get_class_info(bjxnxq,bjxsh,bjzyh,nj,pageSize)#获取班级请求
        bj=class_info_dic[self.Class_class_cob.currentText()]#班级编号
        headrs, info_list, page_num=APITool.query_class_info(bjxnxq,bjxsh,bjzyh,nj,bj,pageSize)
        #设置视图
        self.Init_list_view(headrs, self.Class_view, info_list, self.Class_course_info_lab, page_num)
        self.In_the_view_btn(self.Class_view, pageSize, 5)
        # 设置表格列宽
        self.Class_view.setColumnWidth(1, 134)
        self.Class_view.setColumnWidth(2, 174)
        self.Class_view.setColumnWidth(3, 171)
        self.Class_view.setColumnWidth(4, 154)
        #设置按钮显示
        totalpage = re.findall(".*/(.*)页.*", self.Class_course_info_lab.text())[0]  # 总页数

        if totalpage=="1":
            self.Class_next_btn.setEnabled(False)
            self.Class_endpage_btn.setEnabled(False)
        else:
            self.Class_next_btn.setEnabled(True)
            self.Class_endpage_btn.setEnabled(True)
    #班级课表首页
    def ret_class_first(self):
        totalrows = re.findall(".*共(.*)项.*", self.Class_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.Class_course_info_lab.text())[0]  # 总页数
        self.current_page = 1
        page = str(self.current_page)
        pageSize = self.Class_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_class_info(totalrows, page, pageSize)
        # 设置视图
        self.Init_list_view(headrs, self.Class_view, info_list, self.Class_course_info_lab, page_num)
        self.In_the_view_btn(self.Class_view, pageSize, 5)
        # 设置表格列宽
        self.Class_view.setColumnWidth(1, 134)
        self.Class_view.setColumnWidth(2, 174)
        self.Class_view.setColumnWidth(3, 171)
        self.Class_view.setColumnWidth(4, 154)

        # 设置控件显示
        self.Class_firstpage_btn.setEnabled(False)
        self.Class_Previous_btn.setEnabled(False)
        self.Class_next_btn.setEnabled(True)
        self.Class_endpage_btn.setEnabled(True)
        if totalpage == "1" or totalpage == "0":
            self.Class_next_btn.setEnabled(False)
            self.Class_endpage_btn.setEnabled(False)
    #班级课表上一页
    def ret_class_Previous(self):
        self.current_page = self.current_page - 1
        totalrows = re.findall(".*共(.*)项.*", self.Class_course_info_lab.text())[0]  # 总项数
        page = str(self.current_page)
        pageSize = self.Class_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_class_info(totalrows, page, pageSize)

        # 设置视图
        self.Init_list_view(headrs, self.Class_view, info_list, self.Class_course_info_lab, page_num)
        self.In_the_view_btn(self.Class_view, pageSize, 5)
        # 设置表格列宽
        self.Class_view.setColumnWidth(1, 134)
        self.Class_view.setColumnWidth(2, 174)
        self.Class_view.setColumnWidth(3, 171)
        self.Class_view.setColumnWidth(4, 154)
        #设置按钮显示
        self.Class_next_btn.setEnabled(True)
        self.Class_endpage_btn.setEnabled(True)
        print(page)
        if page == "1":
            self.Class_firstpage_btn.setEnabled(False)
            self.Class_Previous_btn.setEnabled(False)
    #班级课表下一页
    def ret_class_Next(self):
        self.current_page = self.current_page + 1
        totalrows = re.findall(".*共(.*)项.*", self.Class_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.Class_course_info_lab.text())[0]  # 总页数
        page = str(self.current_page)
        pageSize = self.Class_page_cob.currentText()[:-1]
        headrs, info_list, page_num=APITool.get_replace_class_info(totalrows,page,pageSize)

        # 设置视图
        self.Init_list_view(headrs, self.Class_view, info_list, self.Class_course_info_lab, page_num)
        self.In_the_view_btn(self.Class_view, pageSize, 5)
        # 设置表格列宽
        self.Class_view.setColumnWidth(1, 134)
        self.Class_view.setColumnWidth(2, 174)
        self.Class_view.setColumnWidth(3, 171)
        self.Class_view.setColumnWidth(4, 154)

        # 设置显示按钮
        self.Class_firstpage_btn.setEnabled(True)
        self.Class_Previous_btn.setEnabled(True)
        if page == totalpage:
            self.Class_next_btn.setEnabled(False)
            self.Class_endpage_btn.setEnabled(False)
    #班级课表尾页
    def ret_class_End(self):
        # 传递以及获取对应的数据
        totalrows = re.findall(".*共(.*)项.*", self.Class_course_info_lab.text())[0]  # 总项数
        totalpage = re.findall(".*/(.*)页.*", self.Class_course_info_lab.text())[0]  # 总页数
        self.current_page = int(totalpage)
        page = str(self.current_page)
        pageSize = self.Class_page_cob.currentText()[:-1]
        headrs, info_list, page_num = APITool.get_replace_class_info(totalrows, page, pageSize)

        # 设置视图
        self.Init_list_view(headrs, self.Class_view, info_list, self.Class_course_info_lab, page_num)
        self.In_the_view_btn(self.Class_view, pageSize, 5)
        # 设置表格列宽
        self.Class_view.setColumnWidth(1, 134)
        self.Class_view.setColumnWidth(2, 174)
        self.Class_view.setColumnWidth(3, 171)
        self.Class_view.setColumnWidth(4, 154)

        # 设置显示按钮
        self.Class_firstpage_btn.setEnabled(True)
        self.Class_Previous_btn.setEnabled(True)
        self.Class_next_btn.setEnabled(False)
        self.Class_endpage_btn.setEnabled(False)
    def Grade_query_Page(self, index):
        if index == 0:  # 全部及格成绩
            self.all_pass_grade()
        elif index == 1:  # 课程属性成绩
            self.set_course_attribute_score()
        elif index == 2:  # 方案成绩
            self.set_plan_score()
        elif index == 3:#不及格成绩
            self.all_nopass_grade()
        elif index == 4:  # 本学期成绩
            self.get_this_semester_info()
        elif index == 5:#本学期课程安排
            self.Init_course_arrange()
        elif index == 6: #课程基本信息
            self.set_course_info_page()
    #教学资源页面切换
    def Education_resources_Page(self,index):
        if index == 0:  #教室课表
            self.Init_Classroom_Schedule_info()
        elif index == 1: #教师课表
            self.Init_teacher_curriculum_info()
        elif index == 2: #班级课表
            self.Init_class_curriculum_info()
        elif index == 3:#课程课表
            self.Init_course_curriculum_info()
    #tab切换标签槽函数(主界面)
    def Main_Page(self,index):
        self.flag=False
        if index==0:#个人主页
            self.img_info()
            self.personal_info()
        elif index==1:#课程管理
            self.Select_course(4)
        elif index==2:#教学评估
            pass
        elif index==3:#教学资源
            self.Init_Classroom_Schedule_info()
        elif index==4:#综合查询
            self.list_and_view_date()
            self.all_pass_grade()
        elif index==5:#学分绩点
            self.start_cmbox.clear()#清空下拉列表,防止重复添加数据
            self.end_cmbox.clear()
            self.get_group_point()
        else:
            self.info_ted.clear()
    #选课计划课程页面
    def show_planning_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.Planning_course_Page)#跳转到相应的页面
        headrs=['课程号'	 ,'课程名'	 ,'课序号'	 ,'学分',	 '课程属性'	, '考试类型	', '上课教师',	 '课余量'	, '选课模式'	, '选课控制',	 '选课限制说明',	'选择']
        res_list=[]#待教务处更新请求
        self.select_course_data(self.Planning_course_view,headrs,res_list)
    #选课方案课程页面
    def show_program_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.Program_course_Page)  # 跳转到相应的页面
        headrs = ['选择',	'计划学年学期'	,'课程号',	'课程名',	'课序号',	'学分'	,'课程属性',	'考试类型'	,'教师'	,'课余量',	'选课模式	','选课控制',	'选课限制说明	','周次',	'星期	','节次',	'节数'	,'校区',	'教学楼',	'教室']
        res_list = []  # 待教务处更新请求
        self.select_course_data(self.Program_course_view, headrs, res_list)
    #选课系任选课页面
    def show_elective_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.Elective_course_Page)  # 跳转到相应的页面
        headrs = ['选择',	'选课课组'	,'课程号',	'课程名',	'课序号',	'学分'	,'课程属性',	'考试类型'	,'教师'	,'课余量',	'选课模式	','选课控制',	'选课限制说明	','周次',	'星期	','节次',	'节数'	,'校区',	'教学楼',	'教室']
        res_list = []  # 待教务处更新请求
        self.select_course_data(self.Elective_course_view, headrs, res_list)
    #选课校任选课页面
    def show_school_elective_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.School_elective_course_Page)  # 跳转到相应的页面
        headrs = ['选择',	'选课课组'	,'课程号',	'课程名',	'课序号',	'学分'	,'课程属性',	'考试类型'	,'教师'	,'课余量',	'选课模式	','选课控制',	'选课限制说明	','周次',	'星期	','节次',	'节数'	,'校区',	'教学楼',	'教室']
        res_list = []  # 待教务处更新请求
        self.select_course_data(self.School_elective_course_view, headrs, res_list)
    #选课自由选择页面
    def show_free_choice_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.free_choice_course_Page)  # 跳转到相应的页面
        headrs = ['选择',	'开课系'	,'课程号',	'课程名',	'课序号',	'学分'	,'课程属性',	'考试类型'	,'教师'	,'课余量',	'选课模式	','选课控制',	'选课限制说明	','周次',	'星期	','节次',	'节数'	,'校区',	'教学楼',	'教室']
        res_list = []  # 待教务处更新请求
        self.select_course_data(self.free_choice_course_view, headrs, res_list)
    #选课重修课程页面
    def show_rehearsal_course_page(self):
        self.stackedWidget_2.setCurrentWidget(self.Rehearsal_course_Page)  # 跳转到相应的页面
        headrs = ['选择',	'计划学年学期'	,'课程号',	'课程名',	'课序号',	'学分'	,'课程属性',	'考试类型'	,'教师'	,'课余量',	'选课模式	','选课控制',	'选课限制说明	','周次',	'星期	','节次',	'节数'	,'校区',	'教学楼',	'教室']
        res_list = []  # 待教务处更新请求
        self.select_course_data(self.Rehearsal_course_view, headrs, res_list)
    #选课数据处理
    def select_course_data(self,view,headrs,res_list):
        model = QStandardItemModel(view)
        model.setColumnCount(len(headrs))
        for idx, title in enumerate(headrs):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        view.setModel(model)
    #校历页面
    def show_School_calendar(self):
        self.About_page.show()
    #休学页面
    def show_Suspension_Page(self):
        self.About_Suspension_page.show()
    #复学办理流程页面
    def show_return_to_school(self):
        self.About_return_school_page.show()
    #退学办理页面
    def show_Drop_out_school(self):
        self.About_Drop_out_page.show()
    #补办学位证页面
    def show_Reissue_degree(self):
        self.About_Reissue_page.show()
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)

    window=Edt_sys()
    window.show()

    sys.exit(app.exec_())