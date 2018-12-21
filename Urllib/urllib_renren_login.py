# coding:utf-8
import urllib2
import urllib

# 可以做cookie的持久化存储
import cookielib


def send_request():
    ### 1. 发送登录的post请求，并获取登录的cookie

    # renren网登录接口，只需要提供账户和密码即可
    post_url = "http://www.renren.com/PLogin.do"

    # 构建账户密码的表单数据
    form_dict = {
        "email": "mr_mao_hacker@163.com",
        "password": "ALARMCHIME"
    }

    form_data = urllib.urlencode(form_dict)
    # 构建请求报头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 构建一个附带账户密码的post请求对象
    request = urllib2.Request(post_url, data=form_data, headers=headers)

    # 构建一个cookiejar对象,用来保存产生的cookie
    cookie_jar = cookielib.CookieJar()
    # 使用cookiejar对象构建自定义的handler对象
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 使用处理器,构建自定义的opener对象
    opener = urllib2.build_opener(cookie_handler)
    # 发送post请求并记录产生的cookie
    opener.open(request)

    #### 2. 使用登录的cookie，发送其他页面的请求，可以访问需要登录权限的页面
    url_list = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile"
    ]

    for index, url in enumerate(url_list):
        request = urllib2.Request(url, headers=headers)
        response = opener.open(request)

        with open(str(index) + ".html", "w") as f:
            f.write(response.read())


if __name__ == '__main__':
    send_request()