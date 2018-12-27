# coding:utf-8
# 通过请求头发送cookie

### 注意:scrapy中cookie放入headers中不生效,需要单独提出来

import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren_cookies"
    # allowed_domains =[]
    start_urls= [
        "http://www.renren.com/893897109/profile",
        "http://www.renren.com/890297976/profile"
    ]

    cookies = {
       "anonymid": "jpksloq576khwr",
       "_r01_": "1",
       "_de": "357231A48437FE1A247380B22A94C474696BF75400CE19CC",
       "__utma": "151146938.1908916267.1544596057.1544596057.1544596057.1",
       "__utmz": "151146938.1544596057.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
       "ln_uact": "67056665@qq.com",
       "ln_hurl": "http://hdn.xnimg.cn/photos/hdn121/20121209/2000/h_main_dkJa_7e50000042161375.jpg",
       "jebe_key": "f8ec8a51-b9c5-4c06-b1dc-2cf7de00f7cf%7C60eaa7a2aa1b3966a819f29c5fb94eae%7C1544596211030%7C1%7C1544596209079",
       "wp": "0",
       "depovince": "GW",
       "jebecookies": "8f254fd0-c5e8-413b-9f00-617538dc4e83|||||",
       "JSESSIONID": "abc96I63rX2hm89VXkKFw",
       "ick_login": "26b0e98e-80ea-458c-b40f-0e1a31e3043c",
       "p": "e9d85a0f7a421400e57a58207e3ce4a69",
       "first_login_flag": "1",
       "t": "c25a6565cc20f39390348e8d183c67b89",
       "societyguester": "c25a6565cc20f39390348e8d183c67b89",
       "id": "335684059",
       "xnsid": "1bd4d7ae",
       "loginfrom": "syshome",
       "ch_id": "10016",
       "wp_fold": "0",
       "jebe_key": "f8ec8a51-b9c5-4c06-b1dc-2cf7de00f7cf%7C60eaa7a2aa1b3966a819f29c5fb94eae%7C1544596211030%7C1%7C1545721470233"
    }

    headers = {
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
       "Accept-Encoding": "gzip, deflate",
       "Accept-Language": "zh-CN,zh;q=0.9",
       "Connection": "keep-alive",
       "Host": "www.renren.com",
       "Referer": "http://www.renren.com/335684059/profile",
       "Upgrade-Insecure-Requests": "1",
       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"
    }

    # 重写父类中start_requests方法
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, headers=self.headers, callback=self.parse)


    def parse(self, response):
        title = response.xpath("//title/text()").extract_first()

        with open(title + ".html", "w") as f:
            f.write(response.body)  # body取响应体内容


