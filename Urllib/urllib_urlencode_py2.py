# coding:utf-8

# 处理请求构建
import urllib2
# 处理url编码转换
import urllib

def send_request(key_word):
    # 固定不变的url部分
    base_url = "https://www.baidu.com/s?"

    query_dict = {"wd": key_word}

    # urlencode()接受一个字典,并构建查询字符串
    query_str = urllib.urlencode(query_dict)

    # https://www.baidu.com/s?wd=%E7%A7%A6%E6%97%B6%E6%98%8E%E6%9C%88
    full_url = base_url + query_str

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(full_url, headers=headers)
    response = urllib2.urlopen(request)

    # 获取网页原始编码字符串(utf-8, bytes类型)
    return response.read()

if __name__ == '__main__':
    key_word = raw_input("请输入要查询的内容:")
    html = send_request(key_word)

    with open("baidu.html", "wb") as f:
        f.write(html)



