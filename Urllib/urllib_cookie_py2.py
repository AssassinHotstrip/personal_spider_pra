# coding:utf-8
import urllib2

def send_request():
    url_list = [
        "http://www.renren.com/335682222/profile",
        "http://www.renren.com/376602223/profile"
    ]

    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               # "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9",
               "Cache-Control": "max-age=0",
               "Connection": "keep-alive",
               # 重点：通过抓包获取登录用户的cookie，可以直接访问登录后才能访问的页面
               "Cookie": "anonymid=jpksloq576khwr; depovince=GW; _r01_=1; JXsgHEw; ick_login=9c4b2fwf53c-4585-4fwerew454554c-8a4537b-4868da280f90; _de=357231A48437FE1A247380B22A94C474696BF75400CE19CC; ick=73a512c4-e2a6-4cb4-8b38-ca91b727329c; __utma=15114tewtwf6938.1908916267.1544596057.1544596057.1544596057.1; __utmc=151wrewr146938; __utmz=151146938.1544596057.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=wefwf|utmcct=/; __utmb=151146938.4.10.1544596057; jebecookies=74e6c1e6-9b9a-48ef-97a6-d243984caecc|||||; p=39f8205f846d7651e5637fewfwf5402bc0e4ef9; first_login_flag=1; ln_uact=655654191@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20121209/2000/h_main_dkJa_7e500fwf00042161375.jpg; t=03ca85b59ewrrwr3420ba7f6fe9889; societyguester=03ca85b5fwf9db08585eb84a0ba7f6fe9889; id=335684059; xnsid=5ee445ea; loginfrom=syshome; ch_id=10016; jebe_key=f8ec8a51-b9c5-4c06-b1dc-2cf7de00f7cf%7C60eaa7a2aa1b3966a819f29c5fb94eae%7C1544596211030%7C1%7C1544596209079; wp_rewrwfold=0; ewrwe",
               "Host": "www.renren.com",
               "Referer": "http://friend.renren.com/managefriends",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"
               }

    for index, url in enumerate(url_list):
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        with open(str(index)+".html", "w") as f:
            f.write(response.read())




if __name__ == '__main__':
    send_request()