import sys
import requests
import base64


def banner():
    print("""fofa api

  ______ ____  ______      
 |  ____/ __ \|  ____/\    
 | |__ | |  | | |__ /  \   
 |  __|| |  | |  __/ /\ \  
 | |   | |__| | | / ____ \ 
 |_|    \____/|_|/_/    \_\
                           
                           
e.g python fofaapi.py fofa语法 获取页码 每页个数
python fofa.py xxx.com 1 10
常用语法：①  domain="domain"
        ②  icp.name="企业名"
        ③  ip="xx.xx.xx.xx/24"
        ④  status_code="200"
        ⑤  cert.sha-1="be7605a3b72b60fcaa6c58b6896b9e2e7442ec50"
请求后的格式为：url ip port 
        """)


def request1():
    target = baseSearch(sys.argv[1])
    email = ""
    key = ""
    page = sys.argv[2]
    size = sys.argv[3]
    re1 = "https://fofa.info/api/v1/search/all?email=%s&key=%s&" \
          "qbase64=%s&page=%s&size=%s&" \
          "full=false" % (email, key, target, page, size)
    res = requests.get(re1)
    for i in res.json().get('results'):
        url = i[0]
        ip = i[1]
        port = i[2]
        print(f'{url} {ip} {port} ')


def baseSearch(string1):
    return str(base64.b64encode(string1.encode('utf8')), 'utf-8')


if __name__ == "__main__":
    banner()
    request1()
