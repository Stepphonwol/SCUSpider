# coding:utf-8
import requests
from parser import Parser

class Intruder:
    def __init__(self):
        self.login_url = 'http://202.115.47.141/login.jsp'
        self.user_url = 'http://202.115.47.141/loginAction.do'
        self.grade_url = 'http://202.115.47.141/gradeLnAllAction.do?type=ln&oper=fa'
        self.id = input("Account：")
        self.password = input("Password：")
        #3310

    def login(self):
        load = requests.Session()
        form_data = {
            'zjh' : self.id,
            'mm' : self.password
        }
        load.post(self.user_url, form_data)
        return load

    def score_page(self):
        try:
            load = self.login()
            first_response = load.get(self.grade_url)
            borrow_parser = Parser(first_response.text)
            real_url = borrow_parser.get_real_url()
            second_response = load.get(real_url)
            html = second_response.text
            #print(html)
            return html
        except:
            print("Login error !!!")
            return None

    def GPA(self):
        p = Parser(self.score_page())
        p.get_course()
        p.show_courses()
        p.calc_all_GPA()
        p.calc_compulsory_GPA()
        #p.show()

if __name__ == '__main__':
    test = Intruder()
    test.GPA()
'''
def acquire_html(url):
    headers = {
        'Referer' : 'http://jwc.scu.edu.cn/',
        'Host' : 'jwc.scu.edu.cn',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection' : 'keep - alive',
        'Accept-Language' : 'zh - cn',
        'Accept-Encoding' : 'gzip,deflate',
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_6) AppleWebKit/ 604.5.6(KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
        'Cookie' : 'JSESSIONID=7E0C5077185BCC91647D27EF1B5585DD;FSSBBIl1UgzbN7N80T=1e2fDJUs67xmo1fCN_M1Ufx6cnHzuHaq5yyfVz.V1fE.Oxdq2zbqZIiBhP3q6997FQyehkos5aKcNdAsEEZ6etNQYzSLNUpI3RjvuDnQ8opIkNe4ukox0rahfGJhqNSCeKb10Aj3HwHQA72vBu97zsiC2X.FYCdlDGag5VwrTUZixHEId8FcSoXylux5P4VVqKaXsD8i0Deh7SmQMuMl2tKW0fIfWUYm8rSZqRzX1UOq7ejHY54Z62SG4KExlfBZDhwPbgdRKurwy7E31bTRI1w25azKGQpTTQ2snLfXBIC2TYpWxIdxxFxyQT2KAhYE4hJKgAss1VnZluDoS0HUrcPHz;JSESSIONID=7D2120801CD3E2C186EDFB20C8F18213;FSSBBIl1UgzbN7N80S=6uCwsVjbXzVZlg5mE6cyG6U.0AZw4voDwqMQQcyUWjbC7ERzQ4mb8fQpqV3jLt5D'
    }
    #cookies = dict(cookies_are='JSESSIONID=82015F6DC15C095D1245035385239B16;FSSBBIl1UgzbN7N80T=1NGGKR11vgWlUD96yX8soTWC1bt7OMTrXzZGlyXYcTJjuw_rTyOr7hhXMCwrvafztEZZMUc1X9sky.Y13QyCz87wmW_0Wdgj2sPTqK8672buidQefKBtlkzOHmIv_VgiadXmBAV1rVPXzZDSUtGq4deoG36TMeSIcq.0LUyX6YirnMot71eSI_LJ9NAjh28uPVnakpqeLAl88ooHkIB9c8vPQdu0J8yXW..Ajc_ubtj8kdiZw2.esM4SSFzIjE0ZpD06ztbZ9Epw0prLCfrP8uC9VCCaZWDj28K0EbP1S_alB7X3R8yoyuhqoI_i9RyXa18O7vwIcbovaQKSEnxzzp9jp;JSESSIONID=7D2120801CD3E2C186EDFB20C8F18213;FSSBBIl1UgzbN7N80S=6uCwsVjbXzVZlg5mE6cyG6U.0AZw4voDwqMQQcyUWjbC7ERzQ4mb8fQpqV3jLt5D')
    #s = requests.Session()
    #s.get(url, headers=headers, timeout=3)
    #response = requests.get(url, headers=headers, timeout=3)
    response = requests.get(url, headers=headers, timeout=3)
    print(response.status_code)
    print(response.text)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    test = soup.find_all("a", target = "_blank")
    for t in test:
        print(t['href'])

if __name__ == "__main__":
    url = 'http://jwc.scu.edu.cn/jwc/frontPage.action'
    #url = 'http://www.baidu.com'
    html = acquire_html(url)
    parse_html(html)
'''