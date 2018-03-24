## SCUSpider
#### 爬取源网页：四川大学学生教务系统
>
    self.login_url = 'http://202.115.47.141/login.jsp'
    self.user_url = 'http://202.115.47.141/loginAction.do'
    self.grade_url = 'http://202.115.47.141/gradeLnAllAction.do?type=ln&oper=fa'

#### 爬取目标：计算四川大学学生绩点
#### 爬取过程：登录，获取含有课程信息的URL, 解析， 计算
##### 登录
- 使用requests库的Session类获取cookie信息，再登录
>
    def login(self):
        load = requests.Session()
        form_data = {
            'zjh' : self.id,
            'mm' : self.password
        }
        load.post(self.user_url, form_data)
        return load

##### 获取含有课程信息的URL
- 获取培养方案号（培养方案不同的学生，相应的目标URL也不同)
>
    def get_real_url(self):
        s = BeautifulSoup(self.html, 'lxml')
        dict = {'name':'lnfaIfra', 'width':'100%', 'height':'490', 'scrolling':'0', 'frameborder':'0', 'align':'center'}
        fajhh_html = s.find('iframe', attrs=dict)
        fajhh = fajhh_html['src'].strip()
        #print(fajhh)
        real_url = "http://202.115.47.141/" + fajhh
        #print(real_url)
        return real_url

##### 解析
- 使用BeautifulSoup找出需要爬取的课程信息
>
    course_table = self.soup.find_all('td', align='center')

##### 计算
- 根据四川大学绩点计算方法和已爬取到的课程信息，计算绩点

#### 运行截图：
![](5.14.19.png)

#### 源代码列表：
- intruder.py
- parser.py
 

