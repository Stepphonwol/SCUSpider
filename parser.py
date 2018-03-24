# coding:utf-8
from bs4 import BeautifulSoup

class Course:
    def __init__(self, id, seq, name, credit, attr, grade):
        self.id = id
        self.seq = seq
        self.name = name
        self.credit = credit
        self.attr = attr
        self.grade = grade


class Parser:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, 'lxml')
        self.cont = []
        print("Initializing parser...")

    def get_real_url(self):
        s = BeautifulSoup(self.html, 'lxml')
        dict = {'name':'lnfaIfra', 'width':'100%', 'height':'490', 'scrolling':'0', 'frameborder':'0', 'align':'center'}
        fajhh_html = s.find('iframe', attrs=dict)
        fajhh = fajhh_html['src'].strip()
        #print(fajhh)
        real_url = "http://202.115.47.141/" + fajhh
        #print(real_url)
        return real_url

    def get_course(self):
        course_table = self.soup.find_all('td', align='center')
        temp_cont = []
        #for i in course_table:
            #if i.string is not None:
                #print(i.string.strip(), '\n')
        for i, item in enumerate(course_table):
            if len(temp_cont) == 5:
                c = Course(temp_cont[0], temp_cont[1], temp_cont[2], temp_cont[3], temp_cont[4], 0)
                temp_cont.clear()
                self.cont.append(c)
            if item.string is not None:
                if i % 7 == 0:
                    id = item.string.strip()
                    temp_cont.append(id)
                    #print("id: ", id)
                elif i % 7 == 1:
                    seq = item.string.strip()
                    temp_cont.append(seq)
                    #print("seq: ", seq)
                elif i % 7 == 3:
                    name = item.string.strip()
                    temp_cont.append(name)
                    #print("name: ", name)
                elif i % 7 == 4:
                    credit = item.string.strip()
                    temp_cont.append(credit)
                    #print("credit: ", credit)
                elif i % 7 == 5:
                    attr = item.string.strip()
                    temp_cont.append(attr)
                    #print("attr: ", attr)
        course_grade = self.soup.find_all('p', align='center')
        #print(len(course_grade), len(self.cont))
        for i, item in enumerate(course_grade):
            if i % 2 == 0:
                self.cont[i // 2].grade = item.string.strip()
            #print(i, item)
            #print(item.string.strip())
            #self.cont[i].grade = item.string.strip()

    def grade_to_point(self, grade):
        if grade == '优秀':
            return 4.0
        elif grade == '良好':
            return 3.3
        grade = float(grade)
        if grade >= 90:
            return 4.0
        elif grade >= 85:
            return 3.7
        elif grade >= 80:
            return 3.3
        elif grade >= 76:
            return 3
        elif grade >= 73:
            return 2.7
        elif grade >= 70:
            return 2.3
        elif grade >= 66:
            return 2
        elif grade >= 63:
            return 1.7
        elif grade >= 60:
            return 1.3
        elif grade < 60:
            return 0

    def calc_compulsory_credits(self):
        sum = 0
        for item in self.cont:
            if item.attr == '必修':
                sum = sum + int(item.credit)
        return sum

    def calc_all_credits(self):
        sum = 0
        for item in self.cont:
            sum = sum + int(item.credit)
        return sum

    def calc_compulsory_GPA(self):
        sum = 0
        for item in self.cont:
            if item.attr == "必修":
                sum = sum + self.grade_to_point(item.grade) * int(item.credit)
        gpa = sum / self.calc_compulsory_credits()
        print("Compulsory GPA: ", gpa)

    def calc_all_GPA(self):
        sum = 0
        for item in self.cont:
            sum = sum + self.grade_to_point(item.grade) * int(item.credit)
        gpa = sum / self.calc_all_credits()
        print("All GPA: ", gpa)

    def show_courses(self):
        for item in self.cont:
            print(item.id, item.seq, item.name, item.credit, item.attr, item.grade)