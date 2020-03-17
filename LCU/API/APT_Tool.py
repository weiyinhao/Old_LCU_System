from PyQt5.Qt import *
import requests
import os
from bs4 import BeautifulSoup
#封装URL类
class API(object):

    #聊城大学网站端口地址
    header_url="http://jwcweb.lcu.edu.cn/"
    #仿浏览器登录
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    #个人培养方案GET
    TRA_PRO_URL=header_url+"xxInfoAction.do?type={}&infoType=fajhInfo&fajhh={}"

    # 验证码 GET
    YZM_URL = header_url+"validateCodeAction.do?random="

    # 登录验证 POST
    # zjh1:
    # tips:
    # lx:
    # evalue:
    # eflag:
    # fs:
    # dzslh:0
    # zjh:
    # mm:
    # v_yzm: Lxrh
    LOGIN_URL = header_url+"loginAction.do"

    # 个人照片 GET
    IMG_URL = header_url+"xjInfoAction.do?oper=img"

    # 个人信息 GET
    SELF_INFO_URL = header_url+"xjInfoAction.do?oper=xjxx"

    # 网上选课 GET
    NETWORK_SELECT_COURSE_URL = header_url+"xkAction.do"

    # 选课结果 GET
    SELECT_COURSE_RES_URL = header_url+"xkAction.do?actionType=6"

    # 退课 GET
    DROP_COURSE_URL = header_url+"xkAction.do?actionType=7"

    # 无效选课结果 GET
    NULL_COURSE_RES_URL = header_url+"xkAction.do?actionType=16"

    # 本学期课表 GET(和选课结果一样的请求)
    CLASS_Schedule_URL = header_url+"xkAction.do?actionType=6"

    # 学分绩点 GET
    GROUP_POINT_URL = header_url+"gradeLnAllAction.do?oper=queryXfjd"

    # 指定时间获取学分绩点 GET
    FIXED_TIMER_GRADE_POINT_URL = header_url+"gradeLnAllAction.do?oper=queryXfjd&ksxnxq={}&jsxnxq={}"

    # 评估公告 GET
    EVALUATE_POST_URL = header_url+"ggglAction.do?actionType=5"

    # 教学评估 GET
    TEACHING_EVALUATE_URL = header_url+"jxpgXsAction.do?oper=listWj"

    # 毕业生评估 GET
    GRADUATE_EVALUATE_URL = header_url+"byspgXsAction.do?oper=listWj"

    # 总的学期数 GET
    ALL_SCHOOL_TERM_COUNT_URL = header_url+"gradeLnAllAction.do?type=ln&oper=qb"

    # 全部及格成绩 GET
    ALL_PASS_GRADE_URL = header_url+"gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2018-2019%D1%A7%C4%EA%B5%DA%D2%BB%D1%A7%C6%DA(%C1%BD%D1%A7%C6%DA)"

    # 课程属性成绩 GET
    COURSE_ATTRIBUTE_SCORE_URL = header_url+"gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001"

    # 本学期成绩 GET
    THIS_SEMESTER_SCORE_URL = header_url+"bxqcjcxAction.do"

    #方案成绩fajhh参数 GET
    PLAN_SCORE_FAJHH_URL=header_url+"gradeLnAllAction.do?type=ln&oper=fa"
    # 方案成绩 GET
    PLAN_SCORE_URL = header_url+"gradeLnAllAction.do?type=ln&oper=fainfo&fajhh={}"

    # 不及格成绩 GET
    NO_PASS_SCORE_URL = header_url+"gradeLnAllAction.do?type=ln&oper=bjg"

    # 课程基本信息初始化页面 GET
    COURSE_INFO_URL = header_url+"kclbAction.do"

    # 课程基本信息查询 POST
    # kkxsh:
    # kclbdm:
    # kch:
    # kcm:
    # pageSize: 20
    # page: 1
    # currentPage: 1
    # pageNo:
    QUERY_COURSE_INFO_URL = header_url+"kclbAction.do?oper=kclb"

    # 课程基本信息按钮相关(上一页 下一页 首页等)的请求 GET
    # http://210.44.113.70/kclbAction.do?totalrows=16584&page=2&pageSize=20
    NEW_COURSE_INFO_URL = header_url+"kclbAction.do?totalrows={}&page={}&pageSize={}"

    # 本学期课程安排 GET
    COURSE_ARRANGE_URL = header_url+"courseSearchAction.do?temp=1"

    # 本学期课程安排提交表单请求 POST
    # org.apache.struts.taglib.html.TOKEN:7470378bb5c3aa45026d01d4a72e1030
    # kch
    # kcm
    # jsm
    # xsjc
    # skxq
    # skjc
    # xaqh
    # jxlh
    # jash
    # pageSize:20
    # showColumn:[…]
    # pageNumber:0
    # actionType1:1
    COURSE_ARRANGE_POST_URL = header_url+"courseSearchAction.do"

    # 本学期课程安排翻页请求  GET
    PAGE_TURNING_URL = header_url+"courseSearchAction.do?actionType=2&pageNumber={}"

    # 教室课表 GET
    CLASSROOM_SCHEDULE_URL = header_url+"jskbcxAction.do?oper=jskb_lb"
    # 教师课表 GET
    TEACH_SCHEDULE_URL = header_url+"lskbcxAction.do?oper=lskb_lb"

    # 教学楼信息 POST
    # js_zxjxjhh: 2018 - 2019 - 2 - 1
    # js_xq: 01
    # js_jxl:
    # js_js:
    # pageSize: 20
    # page: 1
    # currentPage: 1
    # pageNo:
    TEACHING_BUILDING_URL = header_url+"jskbcxAction.do?oper=ld"

    # 教室信息 POST
    # 同上
    CLASSROOM_INFO_URL = header_url+"jskbcxAction.do?oper=ld&xqh={}&jxlh={}"

    # 教室课表 POST
    # 同上
    CLASSROOM_CURRICULUM_URL = header_url+"jskbcxAction.do?oper=cxkb"

    # 教室课表换页 GET
    REPLACE_CLASSROOM_PAGE_URL = header_url+"jskbcxAction.do?totalrows={}&page={}&pageSize={}"

    # 教师课表获取列表 GET
    TEACHER_ACADEMIC_TERM_URL = header_url+"lskbcxAction.do?oper=lskb_lb"

    # 教师信息查询 POST
    # lsxnxq: 2018 - 2019 - 2 - 1
    # lsxsh:
    # lsjsm:
    # pageSize: 20
    # page: 1
    # currentPage: 1
    # pageNo:
    TEACHER_INFO_QUERY_URL = header_url+"lskbcxAction.do?oper=kbtjcx"

    # 教师信息翻页 GET
    REPLACE_TEACHER_INFO_URL = header_url+"lskbcxAction.do?totalrows={}&page={}&pageSize={}"

    # 课程课表页面 GET
    COURSE_CURRICULUM_PAGE_URL = header_url+"kckbcxAction.do?oper=kckb_lb"

    # 课程课表详细信息 POST
    # kcxnxq: 2018 - 2019 - 2 - 1
    # kckcm:
    # xsh: 00
    # kckch:
    # kckxh:
    # pageSize: 20
    # page: 1
    # currentPage: 1
    # pageNo:
    COURSE_CURRICULUM_INFO_URL = header_url+"kckbcxAction.do?oper=kbtjcx"

    # 课程课表翻页 GET
    REPLEACE_COURSE_INFO_URL = header_url+"kckbcxAction.do?totalrows={}&page={}&pageSize={}"

    # 班级课表页面初始信息 GET
    CLASS_CURRICULUM_PAGE_URL = header_url+"bjkbcxAction.do?oper=bjkb_lb"

    # 班级课表显示专业和班级的信息 POST
    # bjxnxq: 2018 - 2019 - 2 - 1
    # bjxsh: 07
    # bjzyh:
    # nj:
    # bj:
    # pageSize: 20
    # page: 1
    # currentPage: 1
    # pageNo:
    PROFESSION_GRADE_INFO_URL = header_url+"bjkbcxAction.do?oper=ld"

    # 查询班级课表信息 POST
    CHECK_CLASS_INFO_URL = header_url+"bjkbcxAction.do?oper=kbtjcx"

    # 班级课表翻页信息 GET
    REPLEACE_CLASS_URL = header_url+"bjkbcxAction.do?totalrows={}&page={}&pageSize={}"
#配置类
class Config(object):
    #验证码图片
    @staticmethod
    def get_yzm_file_path():
        current_path = os.path.realpath(__file__)
        current_dir=os.path.split(current_path)[0]
        return current_dir+r"\yzm.jpg"
    #个人照片
    @staticmethod
    def get_img_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.split(current_path)[0]
        return current_dir + r"\img.jpg"
class APITool(QObject):
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.86 Safari/537.36'
    }
    res={}
    #验证码下载
    @classmethod
    def download_yzm(cls):
        rep=cls.session.get(API.YZM_URL,headers=API.headers)
        yzm_file_path=Config.get_yzm_file_path()
        with open(yzm_file_path,'wb') as f:
            f.write(rep.content)
        return yzm_file_path

    # 个人图片下载
    @classmethod
    def download_Img_info(cls):
        rep = cls.session.get(API.IMG_URL,headers=API.headers)
        img_file_path = Config.get_img_file_path()
        with open(img_file_path, 'wb') as f:
            f.write(rep.content)
        return img_file_path
    @classmethod
    def Login(cls,zjh,mm,v_yzm):
        data_dic={
            "zjh1":"",
            "tips":"",
            "lx":"",
            "evalue":"",
            "eflag":"",
            "fs":"",
            "dzslh":"",
            "zjh": zjh,
            "mm": mm,
            "v_yzm": v_yzm
        }
        rep=cls.session.post(API.LOGIN_URL,data=data_dic,headers=API.headers)
        title_info=str(BeautifulSoup(rep.text,"html.parser").title.string)#获取文件头,判断是否登录成功
        return title_info=='学分制综合教务'
    @classmethod
    def check_self_info(cls):
        rep=cls.session.get(API.SELF_INFO_URL,headers=API.headers)
        data_list_key=[]
        data_list_value=[]
        soup=BeautifulSoup(rep.text,"html.parser")#.prettify()#进行格式化
        for child in soup.find_all('td',class_='fieldName'):
            if str(child.string).strip()!='None':
                data_list_key.append(str(child.string).strip().replace(":",""))
        for child in soup.find_all('td',width='275'):
            data_list_value.append(str(child.string).strip())
        res=dict(zip(data_list_key,data_list_value))#把结果合并成字典
        info=str(soup.find('a',style='text-decoration: underline').string).strip()
        cls.res_info=data_list_value
        return res,info
    #培养方案
    @classmethod
    def get_Trapro_info(cls):
        rep = cls.session.get(API.SELF_INFO_URL, headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")  # .prettify()#进行格式化
        trapro_info=str(soup.find('a',style='text-decoration: underline')["onclick"])[13:-56]
        rep=cls.session.get(API.header_url+trapro_info, headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")  # .prettify()#进行格式化
        Course_group_info=str(soup.text).strip().replace(" ","").replace("\r","").replace("\n","")[107:]#去除多余空格
        Course_group_info =Course_group_info.replace("(","").replace(");","").replace('"',"").replace("amp;","")#去除多余的相关字符
        Course_group_list=Course_group_info.split("tree.add")#课组列表信息
        Course_group_list_res=[]#课组信息最终优化结果
        #下面是优化过程
        for each in Course_group_list:
            if each=='':
                continue
            Course_group_list_res.append(each.split(','))
        #print(Course_group_list_res)
        Group_at_res=[]#分组属性
        other_at_res=[]#其它属性
        url_at_res={}#链接属性
        temp=[]#临时列表
        #进行数据分解
        for each in Course_group_list_res:
            if each[1]=='-1':
                Group_at_res.append(each[2])
                other_at_res.append(temp)
                temp=[]
            else:#其它属性
                temp.append(each[2])
                url_at_res[each[2]]=each[3]#添加相应课组对应的链接
        other_at_res.append(temp)
        del other_at_res[0]#删除第一个空列表
        dic_res=dict(zip(Group_at_res,other_at_res))#数据压缩 形成字典
        return dic_res,url_at_res
    #获取相应课组信息
    @classmethod
    def get_course_group_info(cls,course_group_url):
        rep = cls.session.get(API.header_url+course_group_url, headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")  # .prettify()#进行格式化
        course_info=[]
        Course_plan_info=[]
        res_info=[]
        for each in soup.find_all('p',align='left'):
            course_info.append(str(each.string).strip())
        for each in soup.find_all('td'):
            res=str(each.string).strip().replace("None","").replace("\r","").replace("\n","").replace(" ","").replace("课程基本信息","")
            Course_plan_info.append(res)
        for i in range(len(Course_plan_info)):
            if Course_plan_info[i]=='' or Course_plan_info[i]=='课程方案信息' or Course_plan_info[i]=='计划学年' or Course_plan_info[i]=='计划学期' or Course_plan_info[i]=='课程属性' or Course_plan_info[i]=='考试类型' or Course_plan_info[i]=='备注1' or Course_plan_info[i]=='备注2' or Course_plan_info[i]=='备注3' or Course_plan_info[i]=='备注4':
                continue
            res_info.append(Course_plan_info[i])
        #print(res_info)
        return course_info,res_info
    #网上选课
    @classmethod
    def Net_select_course(cls):
        rep=cls.session.get(API.NETWORK_SELECT_COURSE_URL,headers=API.headers)
        title_info = str(BeautifulSoup(rep.text, "html.parser").title.string).strip()  # 获取文件头,判断是否能选课
        if title_info=='错误信息':
            return False
        pass#等待教务处更新 暂时无法获取请求
    #退课信息
    @classmethod
    def Drop_course(cls):
        rep = cls.session.get(API.DROP_COURSE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        #print(soup.text)
        title_info = str(BeautifulSoup(rep.text, "html.parser").title.string).strip()  # 获取文件头,判断是否能选课
        if title_info == '错误信息':
            return None
        # 退课基本信息
        headers_info_list=['操作','培养方案','课程号','课程名','课序号','学分','课程属性','考试类型','教师','修读方式','选课状态','周次','星期','节次','节数','校区','教学楼','教室']
        #退课结果
        DROP_COURSE_RES_LIST=[]
        count=0
        for each in soup.find_all('tr',class_='odd'):
            count=0
            for r in each.find_all('td'):
                count+=1
                if(count==len(headers_info_list)+1):
                    break
                DROP_COURSE_RES_LIST.append(str(r.text).strip())
            if(count==7):
                temp=DROP_COURSE_RES_LIST[-25:-14]
                DROP_COURSE_RES_LIST=DROP_COURSE_RES_LIST[:-7]+temp+DROP_COURSE_RES_LIST[-7:]
        return headers_info_list,DROP_COURSE_RES_LIST
    #无效的选课结果
    @classmethod
    def Null_Course(cls):
        rep = cls.session.get(API.NULL_COURSE_RES_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        title_info = str(BeautifulSoup(rep.text, "html.parser").title.string).strip()  # 获取文件头,判断是否能选课
        if title_info == '错误信息':
            return None
        #无效选课列表
        headers_info_list=[ '课程号','课程名','课序号','课程属性','考试类型', '修读方式','选课状态'	, '选课未成功原因' ,'操作人','操作时间	', '操作人ip']
        #无效选课结果
        null_course_res_list=[]
        return headers_info_list,null_course_res_list
    #选课方案课程页面
    @classmethod
    def Program_course(cls):
        pass
    #选课管理页面
    @classmethod
    def Class_Schedule(cls):
        rep=cls.session.get(API.CLASS_Schedule_URL,headers=API.headers)
        soup=BeautifulSoup(rep.text, "html.parser")
        timer_lab=str(soup.find('td',width='50%',align='right').string).strip()
        #课程表处理
        Course_list=[]
        for each in soup.find_all('tr',bgcolor="#FFFFFF"):
            for r in each.find_all('td'):
                if str(r.get_text()).strip()=='上午' or str(r.get_text()).strip()=='午 休' or str(r.get_text()).strip()=='下午' or str(r.get_text()).strip()=='晚 饭' or str(r.get_text()).strip()=='晚上':
                    continue
                Course_list.append(str(r.get_text()).strip())
        #课程详细信息细节处理
        Course_info_list=[]
        res=soup.find_all('tr',class_='odd')
        count = 0  # 计数
        for each in soup.find_all('tr',class_='odd'):
            count=0
            for r in each.find_all('td'):
                count+=1
                Course_info_list.append(str(r.text).strip())
            if(count==7):#存在多余周次的课程
                temp3=Course_info_list[-25:-14]
                Course_info_list=Course_info_list[:-7]+temp3+Course_info_list[-7:]
            if(count>20):#防止多次选择相同的课程
                break
        '''for each in res[0].find_all('td'):
            #print(str(each.text).strip())
            if len(Course_info_list)%18==0 and str(each.get_text()).strip()!='软件工程2017' and len(Course_info_list)!=0:
                tem=Course_info_list[-18:-7]
                Course_info_list.extend(tem)
            Course_info_list.append(str(each.get_text()).strip())
        #print(Course_info_list)'''
        return (timer_lab,Course_list,Course_info_list)
    @classmethod
    def Check_Group_Point(cls):
        rep=cls.session.get(API.GROUP_POINT_URL,headers=API.headers)
        #每个学期的绩点
        Grade_point_list=[]#保存学分绩点列表
        soup = BeautifulSoup(rep.text, "html.parser")
        res = soup.find_all('tr', class_='odd')
        for each in res:
            for info in each.find_all('td', align="center"):
                if str(info.string).strip()!='None':
                    Grade_point_list.append(str(info.string).strip())

        #获取当前平均绩点
        Grade_point_value=soup.find('input',style='width: 60px;')["value"]#获取平均绩点

        #期间学分绩点查询(开始的学年学期和结束的学年学期一样 不需要再算end了)
        start_academic_term_list=[]
        academic_timer_list=[]
        start_academic_term_res=soup.find('select',id="ksxnxq")
        for each in  start_academic_term_res.find_all('option'):
            start_academic_term_list.append(str(each.get_text()).strip())
            academic_timer_list.append(each["value"])
        academic_term_dic=dict(zip(start_academic_term_list[1:],academic_timer_list[1:]))#获取学期与学期时间的键值对字典
        return Grade_point_value,Grade_point_list, start_academic_term_list,academic_term_dic
    #查询指定时间内的平均学分绩点
    @classmethod
    def query_fixed_timer_Group_Point(cls,start_timer,end_tiimer):
        rep=cls.session.get(API.FIXED_TIMER_GRADE_POINT_URL.format(start_timer,end_tiimer),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        grade_point_value=soup.find('input',style="width: 60px;",disabled="disabled")["value"]
        return grade_point_value
    #获取总的学期数
    @classmethod
    def query_pass_grade(cls):
        #总学期数
        rep=cls.session.get(API.ALL_SCHOOL_TERM_COUNT_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        school_year_res=soup.find_all('a',target='lnqbIfra')#获取总学期的数量
        school_year_list=[]
        for each in school_year_res:
            school_year_list.append(str(each.text).strip())#保存所有的学年

        #获取所有的及格成绩
        grade_info_list=[]
        rep=cls.session.get(API.ALL_PASS_GRADE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        grade_info_res=soup.find_all('tr',class_="odd")
        for each in grade_info_res:
            for r in each.find_all('td',align="center"):
                grade_info_list.append(str(r.text).strip())
        return school_year_list,grade_info_list
    # 获取每个学期的数据
    @classmethod
    def Get_semester_data(cls):
        school_year_list=cls.query_pass_grade()[0]
        rep = cls.session.get(API.ALL_PASS_GRADE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        res_info=soup.find_all('table',class_='titleTop2')
        temp=[]#临时列表
        semester_grade_info_list=[]#二维列表 每一个都是一个学期的列表
        for each in res_info:
            for r in each.find_all('td',align="center"):
                temp.append(str(r.text).strip())
            semester_grade_info_list.append(temp)
            temp=[]
        info_dic=dict(zip(school_year_list,semester_grade_info_list))#打包成字典把每个学期对应的及格成绩
        minimum_credit_list=[]#保存最低修读学分等信息的列表
        res=soup.find_all('td',height="21")#最低修读学分和已修读课程总学分
        for each in res:
            minimum_credit_list.append(str(each.text).strip())
        return info_dic,minimum_credit_list
    #获取课程属性成绩
    @classmethod
    def get_course_attribute_score(cls):
        rep=cls.session.get(API.COURSE_ATTRIBUTE_SCORE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        course_attribute_list=[]#课程属性列表
        course_grade_list=[]#课程成绩列表
        temp=[]#临时列表
        for each in soup.find_all('td',valign="middle"):
            course_attribute_list.append(str(each.text).strip())
        for each in soup.find_all('table',class_='titleTop2'):
            for r in each.find_all('td',align='center'):
                temp.append(str(r.text).strip())
            course_grade_list.append(temp)
            temp=[]
        grade_attribute_dic=dict(zip(course_attribute_list,course_grade_list))
        course_info_list=[]#修读课程总学分
        for each in soup.find_all('td',height="21"):
            course_info_list.append(str(each.text).strip())
        course_info_dic=dict(zip(course_attribute_list,course_info_list))
        return grade_attribute_dic,course_info_dic
    #获取本学期成绩
    @classmethod
    def get_this_semester_score(cls):
        rep=cls.session.get(API.THIS_SEMESTER_SCORE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        this_semester_score_list=[]#保存本学期成绩信息
        for each in soup.find_all('td',align="center"):
            if str(each.text).strip()=="":
                this_semester_score_list.append(" ")
            else:
                this_semester_score_list.append(str(each.text).strip())
        return this_semester_score_list
    #获取不及格的成绩
    @classmethod
    def get_no_pass_score(cls):
        rep=cls.session.get(API.NO_PASS_SCORE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        nopass_info_list=["尚不及格","曾不及格"]
        temp=[]#临时保存数据
        nopass_list=[]#不及格列表
        for each in soup.find_all('table',class_="titleTop2"):
            for r in each.find_all('td',align="center"):
                temp.append(str(r.text).strip())
            nopass_list.append(temp)
            temp=[]
        nopass_dic=dict(zip(nopass_info_list,nopass_list))

        #获取不及格的标签信息
        nopass_lab_list=[]#保存标签信息列表
        for each in soup.find_all('td',height="21"):
            nopass_lab_list.append(str(each.text).strip().replace("\n","").replace("\xa0","").replace("\r","").replace("数                   ","数:").replace("数:                  ","数:"))
        nopass_lab_dic=dict(zip(nopass_info_list,nopass_lab_list))
        print(nopass_lab_dic)
        return  nopass_dic,nopass_lab_dic
    #获取方案成绩
    @classmethod
    def get_plan_socre(cls):
        #获取方案成绩请求的fajhh的token
        reps=cls.session.get(API.PLAN_SCORE_FAJHH_URL,headers=API.headers)
        soups = BeautifulSoup(reps.text, "html.parser")
        token=str(soups.find('iframe',align='center')['src'])[-4:]#得到特定学院的token
        rep=cls.session.get(API.PLAN_SCORE_URL.format(token),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")

        title_info=str(soup.find('td',valign="middle").text).strip()#获取头信息
        take_credits_info=str(soup.find('td',height="21").text).strip()#获取修读学分情况
        group_info=str(soup.find('td',class_="legend").text).strip()#获取GroupBox的标题
        tail_info=""#获取底信息(也是修读情况)
        for each in soup.find_all('font',style="font-weight: bold"):
            tail_info+=str(each.text).strip()+"     "
        course_info_list=[]#保存方案成绩信息列表
        for each in soup.find_all('td',align="center"):
            course_info_list.append(str(each.text).strip())
        return title_info,take_credits_info,group_info,tail_info,course_info_list
    #获取课程基本信息的开课院系和课程类别信息
    @classmethod
    def get_course_department_and_category_info(cls):
        rep=cls.session.get(API.COURSE_INFO_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        department_res=soup.find('select',attrs={"name":"kkxsh"})
        department_res_list=[]#保存所有的开课院系
        department_num_list=[]#开课院系的序列号列表
        for each in department_res.find_all('option'):
            department_res_list.append(str(each.text).strip())
            department_num_list.append(each["value"])
        department_info_dic=dict(zip(department_res_list,department_num_list))#开课院系和对应的序列号的键值对字典
        course_category_res=soup.find('select',attrs={"name":"kclbdm"})
        course_category_list=[]#保存所有的课程类别
        course_category_num_list=[]#保存课程类别的序列号列表
        for each in course_category_res.find_all('option'):
            course_category_list.append(str(each.text).strip())
            course_category_num_list.append(each["value"])
        course_category_dic=dict(zip(course_category_list,course_category_num_list))#保存课程类别的键值对字典
        page_num_res=""#获取当前页数信息
        for s in str(soup.find('td',align="right").text).strip():
            if s=="页":
                page_num_res+="页"
                break
            page_num_res+=s
        return department_info_dic,course_category_dic,page_num_res
    #课程基本信息初始查询信息
    @classmethod
    def query_course_info(cls,kkxsh,kclbdm,kch,kcm,pageSize,page,currentPage):
        data_dic={
            "kkxsh":kkxsh,
            "kclbdm":kclbdm,
            "kch":kch,
            "kcm":kcm,
            "pageSize": pageSize,
            "page": page,
            "currentPage": currentPage,
            "pageNo":""
        }
        rep=cls.session.post(API.QUERY_COURSE_INFO_URL,data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        res_list=[]#保存课程基本信息结果的列表
        for each in soup.find_all('tr',class_="odd"):
            for r in each.find_all('td'):
                res_list.append(str(r.text).strip())
        page_num_res = ""  # 获取当前页数信息
        for s in str(soup.find('td', align="right").text).strip():
            if s == "页":
                page_num_res += "页"
                break
            page_num_res += s
        return res_list,page_num_res

    # 课程基本信息按钮相关(上一页 下一页 首页等)的请求 GET
    @classmethod
    def new_course_info(cls,totalrows,page,pageSize):
        rep=cls.session.get(API.NEW_COURSE_INFO_URL.format(totalrows,page,pageSize),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        res_list = []  # 保存课程基本信息结果的列表
        for each in soup.find_all('tr', class_="odd"):
            for r in each.find_all('td'):
                res_list.append(str(r.text).strip())
        page_num_res = ""  # 获取当前页数信息
        for s in str(soup.find('td', align="right").text).strip():
            if s == "页":
                page_num_res += "页"
                break
            page_num_res += s
        return res_list, page_num_res
    #本学期课程安排初始信息
    @classmethod
    def semester_course_arrange(cls):
        rep=cls.session.get(API.COURSE_ARRANGE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        token=soup.find('input',attrs={'name':'org.apache.struts.taglib.html.TOKEN'})["value"]#获取提交表单的密钥
        Department_key_list=[]#保存院系信息
        Department_value_list=[]#保存院系信息的编码
        department_res = soup.find('select', attrs={"name": "xsjc"})
        for each in department_res.find_all('option'):
            Department_key_list.append(str(each.text).strip())
            Department_value_list.append(str(each["value"]))
        Department_dic=dict(zip(Department_key_list,Department_value_list))
        #上课星期处理
        class_week_key_list=[]#上课日期
        class_week_value_list = []#上课日期的编号
        class_res = soup.find('select', attrs={"name": "skxq"})
        for each in class_res.find_all('option'):
            class_week_key_list.append(str(each.text).strip())
            class_week_value_list.append(each["value"])
        class_week_dic=dict(zip(class_week_key_list,class_week_value_list))

        #上课节次
        class_num_key_list = []  # 上课节次
        class_num_value_list = []  # 上课节次的编号
        class_res = soup.find('select', attrs={"name": "skjc"})
        for each in class_res.find_all('option'):
            class_num_key_list.append(str(each.text).strip())
            class_num_value_list.append(each["value"])
        class_num_dic = dict(zip(class_num_key_list, class_num_value_list))

        #校区
        #每页显示记录数      两个都未做处理 手动添加即可

        #选择要显示的列
        show_col_key_list = []
        show_col_value_list = []
        show_col_res = soup.find('select', attrs={"name": "showColumn"})
        for each in show_col_res.find_all('option'):
            show_col_key_list.append(str(each.text).strip())
            show_col_value_list.append(str(each["value"]))
        show_col_dic = dict(zip(show_col_key_list, show_col_value_list))
        return Department_dic,class_week_dic,class_num_dic,show_col_dic,token
    #课程安排数据获取
    @classmethod
    def get_course_ara_data(cls,soup):
        headrs = ["开课系", "课程号", "课程名", "课序号", "学分", "考试类型", "教师", "周次", "星期", "节次", "校区", "教学楼", "教室", "课容量",
                  "学生数"]  # 保存表格头数据
        course_info_list = []  # 保存课程安排数据
        for each in soup.find_all('tr', class_="odd"):
            for r in each.find_all('td'):
                course_info_list.append(str(r.text).strip())
        for each in soup.find_all('td', align="right"):
            if str(each.text).strip() != "":
                page_num = str(each.text).strip().replace("\xa0", " ").replace("\r", "").replace("\n", "").replace("下一页", "").replace("页1", "").replace("上一页", "")
        return headrs,course_info_list,page_num
    #课程安排首页
    @classmethod
    def course_arrange_info_data(cls,token,kch,kcm,jsm,xsjc,skxq,skjc,xaqh,pageSize,showColumn,pageNumber):
        data_list = [("org.apache.struts.taglib.html.TOKEN", token),
                     ("kch", kch), ("kcm", kcm), ("jsm", jsm.encode("GBK")),
                     ("xsjc", xsjc.encode("GBK")), ("skxq", skxq), ("skjc", skjc),
                     ("xaqh", xaqh), ("jxlh", ""), ("jash", ""),
                     ("pageSize", pageSize),
                     ("showColumn", showColumn[0]),("showColumn", showColumn[1]),
                     ("showColumn", showColumn[2]), ("showColumn", showColumn[3]),
                     ("showColumn", showColumn[4]),("showColumn", showColumn[5]),
                     ("showColumn", showColumn[6]),("showColumn", showColumn[7]),
                     ("showColumn", showColumn[8]), ("showColumn", showColumn[9]),
                     ("showColumn", showColumn[10]),("showColumn", showColumn[11]),
                     ("showColumn", showColumn[12]),("showColumn", showColumn[13]),
                     ("showColumn", showColumn[14]),
                     ("pageNumber","0"),("actionType", "1")]
        rep=cls.session.post(API.COURSE_ARRANGE_POST_URL,data=data_list,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, course_info_list, page_num=cls.get_course_ara_data(soup)
        return headrs,course_info_list,page_num
    #课程安排页面跳转数据处理
    @classmethod
    def Process_Page_turning(cls,current_page_num):
        rep=cls.session.get(API.PAGE_TURNING_URL.format(current_page_num),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, course_info_list, page_num = cls.get_course_ara_data(soup)
        return headrs, course_info_list, page_num
    #教室课表首页
    @classmethod
    def Classroom_Schedule_info_data(cls):
        rep=cls.session.get(API.CLASSROOM_SCHEDULE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        Academic_term_info=soup.find('select',attrs={"name":"js_zxjxjhh"})
        Academic_term_list_key=[]#用来保存学年学期
        Academic_term_list_value=[]#保存学期学年的编号
        for each in Academic_term_info.find_all('option'):
            Academic_term_list_key.append(str(each.text).strip())
            Academic_term_list_value.append(each["value"])
        Academic_term_dic=dict(zip(Academic_term_list_key,Academic_term_list_value))
        Campus_dic={"请选择":"","东校区":"01","西校区":"02"}
        return Academic_term_dic,Campus_dic
    #获取教室课表的教学楼及其编号
    @classmethod
    def get_Teaching_building_data(cls,js_zxjxjhh,js_xq,pageSize):
        data={
            "js_zxjxjhh": js_zxjxjhh,
            "js_xq": js_xq,
            "js_jxl":"",
            "js_js":"",
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo":""
        }
        rep=cls.session.post(API.TEACHING_BUILDING_URL,data=data,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        Teaching_building_list_value=[]#保存教学楼的编号
        Teaching_building_list_key=[]#保存教学楼
        Teaching_building_info=soup.find('select',attrs={"name":"js_jxl"})
        for each in Teaching_building_info.find_all('option'):
            Teaching_building_list_key.append(str(each.text).strip())
            Teaching_building_list_value.append(each["value"])
        Teaching_building_dic=dict(zip(Teaching_building_list_key,Teaching_building_list_value))
        return Teaching_building_dic
    #获取教室课表信息
    @classmethod
    def get_classroom_info(cls,js_zxjxjhh,js_xq,pageSize,js_jxl):
        data_dic={
            "js_zxjxjhh": js_zxjxjhh,
            "js_xq": js_xq,
            "js_jxl": js_jxl,
            "js_js": "",
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo": ""
        }
        rep=cls.session.post(API.CLASSROOM_INFO_URL.format(js_xq,js_jxl),data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        classroom_list_value = []  # 保存教室的编号
        classroom_list_key = []  # 保存教室
        classroom_info = soup.find('select', attrs={"name": "js_js"})
        for each in classroom_info.find_all('option'):
            classroom_list_key.append(str(each.text).strip())
            classroom_list_value.append(each["value"])
        classroom_dic = dict(zip(classroom_list_key, classroom_list_value))
        return classroom_dic

    #获取跳转页面的教室详细信息(封装)
    @classmethod
    def get_replace_page_info(cls,soup):
        headrs = []  # 保存头部数据
        info_list = []  # 保存教室课表信息
        for each in soup.find_all('th', class_="sortable"):
            headrs.append(str(each.text))
        for each in soup.find_all('tr', class_="odd"):
            for r in each.find_all('td'):
                info_list.append(str(r.text).strip())
        page_num = str(soup.find('td', align="right").text).strip()[:15]  # 记录页数
        return headrs,info_list,page_num
    #查询教室课表
    @classmethod
    def query_classroom_curriculum_info(cls,js_zxjxjhh,js_xq,pageSize,js_jxl,js_js):
        data_dic = {
            "js_zxjxjhh": js_zxjxjhh,
            "js_xq": js_xq,
            "js_jxl": js_jxl,
            "js_js": js_js,
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo": ""
        }
        rep=cls.session.post(API.CLASSROOM_CURRICULUM_URL,data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, classroom_info_list, page_num=cls.get_replace_page_info(soup)
        return headrs,classroom_info_list,page_num
    #教室课表换页
    @classmethod
    def replace_classroom_page(cls,totalrows,page,pageSize):
        url_info=API.REPLACE_CLASSROOM_PAGE_URL.format(totalrows,page,pageSize)
        rep=cls.session.get(url_info,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    #教师课表获取基础信息
    @classmethod
    def get_teacher_Basicinfo(cls):
        rep=cls.session.get(API.TEACHER_ACADEMIC_TERM_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        teacher_Init_info_dic={}#保存教师课表学年学期
        for each in soup.find_all('select',attrs={"name":"lsxnxq"}):
            for r in each.find_all('option'):
                teacher_Init_info_dic[str(r.text).strip()]=r["value"]
        Department_info_dic={}#院系信息
        for each in soup.find_all('select',attrs={"name":"lsxsh"}):
            for r in each.find_all('option'):
                Department_info_dic[str(r.text).strip()]=r["value"]
        return teacher_Init_info_dic,Department_info_dic
    #获取教师详细信息
    @classmethod
    def get_teacher_detailedinfo(cls,lsxnxq,lsxsh,lsjsm,pageSize):
        data_dic={
            "lsxnxq":lsxnxq,
            "lsxsh":lsxsh,
            "lsjsm":lsjsm.encode("GBK"),
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo":""
        }
        rep=cls.session.post(API.TEACHER_INFO_QUERY_URL,data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num=cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    #教师课表翻页信息
    @classmethod
    def get_replace_teacherPage_info(cls,totalrows,page,pageSize):
        rep=cls.session.get(API.REPLACE_TEACHER_INFO_URL.format(totalrows,page,pageSize),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    ##获取课程课表详细信息
    @classmethod
    def get_course_detailedinfo(cls,kcxnxq,kckcm,xsh,kckch,kckxh,pageSize):
        cls.session.get(API.COURSE_CURRICULUM_PAGE_URL,headers=API.headers)#先发送课程课表的页面初始化请求，否则后面会出错
        data_dic={
            "kcxnxq":kcxnxq,
            "kckcm":kckcm,
            "xsh": xsh,
            "kckch":kckch,
            "kckxh":kckxh,
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo":""
        }
        rep=cls.session.post(API.COURSE_CURRICULUM_INFO_URL,data=data_dic,headers=API.headers)#发送课程数据请求
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    #获取课程课表的翻页信息
    @classmethod
    def get_replace_course_info(cls,totalrows,page,pageSize):
        rep=cls.session.get(API.REPLEACE_COURSE_INFO_URL.format(totalrows,page,pageSize),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    #获取班级课表的初始信息
    @classmethod
    def get_class_initinfo(cls):
        rep=cls.session.get(API.CLASS_CURRICULUM_PAGE_URL,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        Academic_term_dic={}#保存学年学期
        Dept_dic={}#保存院系
        grade_dic={}#保存年级
        Academic_term_dic,Dept_dic=cls.get_teacher_Basicinfo()
        for each in soup.find_all('select',attrs={"name":"nj"}):
            for r in each.find_all('option'):
                grade_dic[str(r.text).strip()]=r["value"]
        return Academic_term_dic,Dept_dic,grade_dic
    #获取班级课表的专业信息
    @classmethod
    def get_grade_and_pro_info(cls,bjxnxq,bjxsh,pageSize):
        data_dic={
            "bjxnxq": bjxnxq,
            "bjxsh": bjxsh,
            "bjzyh":"",
            "nj":"",
            "bj":"",
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo":""
        }
        rep=cls.session.post(API.PROFESSION_GRADE_INFO_URL,data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        profession_info_dic = {}  # 保存教师课表学年学期
        for each in soup.find_all('select', attrs={"name": "bjzyh"}):
            for r in each.find_all('option'):
                profession_info_dic[str(r.text).strip()] = r["value"]
        return profession_info_dic
    #获取班级课表的班级信息
    @classmethod
    def get_class_info(cls,bjxnxq,bjxsh,bjzyh,nj,pageSize):
        data_dic = {
            "bjxnxq": bjxnxq,
            "bjxsh": bjxsh,
            "bjzyh": bjzyh,
            "nj":nj,
            "bj": "",
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo": ""
        }
        rep = cls.session.post(API.PROFESSION_GRADE_INFO_URL, data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        class_info_dic = {}  # 保存班级信息
        for each in soup.find_all('select', attrs={"name": "bj"}):
            for r in each.find_all('option'):
                class_info_dic[str(r.text).strip()] = r["value"]
        print(class_info_dic)
        return class_info_dic
    #获取班级课表查询信息
    @classmethod
    def query_class_info(cls,bjxnxq,bjxsh,bjzyh,nj,bj,pageSize):
        data_dic={
            "bjxnxq": bjxnxq,
            "bjxsh": bjxsh,
            "bjzyh": bjzyh,
            "nj": nj,
            "bj": bj,
            "pageSize": pageSize,
            "page": "1",
            "currentPage": "1",
            "pageNo": ""
        }
        rep=cls.session.post(API.CHECK_CLASS_INFO_URL,data=data_dic,headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
    #获取班级课表翻页信息
    @classmethod
    def get_replace_class_info(cls,totalrows,page,pageSize):
        rep=cls.session.get(API.REPLEACE_CLASS_URL.format(totalrows,page,pageSize),headers=API.headers)
        soup = BeautifulSoup(rep.text, "html.parser")
        headrs, info_list, page_num = cls.get_replace_page_info(soup)
        return headrs, info_list, page_num
if __name__ == '__main__':
    username = '';
    password = '';
    APITool.download_yzm()
    code=input("验证码：")
    APITool.Login(username,password,code)
    APITool.Class_Schedule()
    #APITool.check_self_info()
