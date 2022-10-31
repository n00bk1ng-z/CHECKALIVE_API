import sys
import requests
import base64


def banner():
    print("""hunter api
  
  _    _ _    _ _   _ _______ ______ _____  
 | |  | | |  | | \ | |__   __|  ____|  __ \ 
 | |__| | |  | |  \| |  | |  | |__  | |__) |
 |  __  | |  | | . ` |  | |  |  __| |  _  / 
 | |  | | |__| | |\  |  | |  | |____| | \ \ 
 |_|  |_|\____/|_| \_|  |_|  |______|_|  \_\
                                            
                                            

e.g python hunter.py hunter语法 获取页码 每页个数
python hunter.py xxx.com 1 10
常用语法：①  domain.suffix="domain"
        ②  icp.name="企业名"
        ③  ip="xx.xx.xx.xx/24"
        ④  header.status_code="200"
        ⑤  cert.sha-1="be7605a3b72b60fcaa6c58b6896b9e2e7442ec50"
请求后的格式为：url ip port web_title domain
        """)


def request1():
    target = baseSearch(sys.argv[1])
    api_key = "" #填写自己的api_key
    page = sys.argv[2]
    size = sys.argv[3]
    re1 = "https://hunter.qianxin.com/openApi/search?api-key=%s&" \
          "search=%s&page=%s&page_size=%s&is_web=1&" \
          "start_time=\"2022-10-01 00:00:00\"&end_time=\"2022-10-31 00:00:00\"" % (api_key, target, page, size)
    res = requests.get(re1)
    for i in res.json().get('data').get('arr'):
        result = []
        url = i.get('url')
        ip = i.get('ip')
        port = i.get('port')
        web_title = i.get('web_title')
        domain = i.get('domain')
        component = i.get('component')
        if component:
            for k in component:
                name = k.get('name')
                version = k.get('version')
                if len(version) == 0:
                    version = "null"
                result.append(f'{name}:{version}')
        print(f'{url} {ip} {port} {web_title} {domain} {";".join(i for i in result)}')


def baseSearch(string1):
    return str(base64.b64encode(string1.encode('utf8')), 'utf-8')


if __name__ == "__main__":
    banner()
    request1()
