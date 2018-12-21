import urllib.request
import urllib.parse

import time
import json
import random
from hashlib import md5

def get_sign(key_word):
    # 时间戳
    ts = str(int(time.time() * 1000))
    # 时间戳加个随机数
    salt = ts + str(random.randint(0, 10))
    # 构建加密参数
    arg = "fanyideskweb" + key_word + salt + "p09@Bn{h02_BIEe]$P^nG"
    # 生成加密参数的 md5
    sign = md5(arg.encode("utf-8")).hexdigest()

    return (ts, salt, sign)


def send_request(key_word):
    """发送请求,返回翻译结果"""
    post_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "272",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "_ntes_nnid=f77d53cb936304b5333b304b767a4958,1506087321856; OUTFOX_SEARCH_USER_ID_NCOO=971893961.4325761; OUTFOX_SEARCH_USER_ID=-1480774266@10.169.0.83; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcbjsSYFJKa5cWGyuwEw; ___rl__test__cookies=1544415498815",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    ts, salt, sign = get_sign(key_word)

    form_dict = {
        "i": key_word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "942cd17bf95d3ff6cb07a988ab9c18f8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false"
    }

    # 构建表单数据
    form_data = urllib.parse.urlencode(form_dict).encode("utf-8")
    # 修改Content-Length
    headers["Content-Length"] = len(form_data)
    # 构建post请求对象
    request = urllib.request.Request(post_url, form_data, headers)
    # 发送POST请求
    response = urllib.request.urlopen(request)

    # 解析响应，提取翻译结果
    result = json.loads(response.read())
    trans_result = result["translateResult"][0][0]["tgt"]
    return trans_result



if __name__ == '__main__':
    key_word = input("请输入要翻译的文本:")
    print(send_request(key_word))