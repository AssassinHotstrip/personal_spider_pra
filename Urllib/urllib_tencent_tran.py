import urllib.request
import urllib.parse
import time
import json


def send_request(key_word):
    # 请求报头
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               # "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive",
               "Content-Length": "287",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": "pgv_pvi=4326192128; RK=+cxAht1AZP; 	ptcz=f85b1fa56e57585a6a05924f38ce10b6b39dd1f144488d88d6fe9efe8dd58070; 	pgv_pvid=2070897366; eas_sid=p1X5K3Q9S984h6f1X3G9M3b0X3; 	ptui_loginuin=2795566911; tvfe_boss_uuid=8b7c812c2890412c; 	pac_uid=1_2795566911; o_cookie=670204191; luin=o0670204191; lskey=0001000	01b20cdff57a739176d014c70e1cf6a51d62effe47a9c5bbe49d9224593a1c2cca0a9b7c0	75da6a78; pt2gguin=o2795566911; 	fy_guid=70d1941f-3a14-49e1-bd11-ca788d54c1f2; pgv_info=ssid=s4815664125; 	ts_refer=www.baidu.com/link; ts_uid=2983128912; 	gr_user_id=2de98a79-dcb3-4e77-882b-4beef5aee4a5; 	9c118ce09a6fa3f4_gr_session_id=b919a914-30fc-46b7-bb54-6b72d66b74e7; 	grwng_uid=322d559d-12d9-4571-91d8-f6794868bfc9; 	8c66aca9f0d1ff2e_gr_session_id=2ac04ce7-9bfb-4780-9f3a-78daa15006fd; 	qtv=c0f5a61daea0816d; qtk=ufWJlIr4+xfV+qCiy+Scf+jGCgak1QnkJid4Byh6xNrt9Kb	nEey1rviJ4VxhvdxOGqZayELSJyP/0rUJ+9UhjaKDOu7CZvHn7mwF/	mu5a3LJDxTeCVYam2B4BHvNF8NgIY0p1AMxJsRGoiO6oGgHew==; 	ts_last=fanyi.qq.com/; openCount=2; 9c118ce09a6fa3f4_gr_session_id_b919a9	14-30fc-46b7-bb54-6b72d66b74e7=true",
               "Host": "fanyi.qq.com",
               "Origin": "https://fanyi.qq.com",
               "Referer": "https://fanyi.qq.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (	KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest"
    }

    # 通过抓包获取的 ajax post请求的url地址
    post_url = "https://fanyi.qq.com/api/translate"

    # 构建自定义的表单数据字典
    form_dict = {"source": "auto",
                 "target": "zh",
                 "sourceText": key_word,
                 "qtv": "c0f5a61daea0816d",
                 "qtk": "ufWJlIr4+xfV+qCiy+Scf+jGCgak1QnkJid4Byh6xNrt9KbnEey1rviJ4VxhvdxOGqZayELSJyP/0rUJ+9UhjaKDOu7CZvHn7mwF/mu5a3LJDxTeCVYam2B4BHvNF8NgIY0p1AMxJsRGoiO6oGgHew==",
                 "sessionUuid": "translate_uuid" + str(int(time.time() * 1000))
    }

    # 构建表单数据字符串
    form_data = urllib.parse.urlencode(form_dict)
    # 修改请求报头里Content - Length长度为当前表单字符串长度
    headers["Content-Length"] = len(form_data)

    # 当Request类提供data参数时，将会构建一个 post请求对象(data参数接收一个bytes类型字符串)
    request = urllib.request.Request(url=post_url, data=form_data.encode("utf-8"), headers=headers)

    response = urllib.request.urlopen(request)

    json_str = response.read()

    result = json.loads(json_str)

    trans_result = result["translate"]["records"][0]["targetText"]

    return trans_result


if __name__ == '__main__':
    key_word = input("请输入要翻译的文本:")
    trans_result = send_request(key_word)
    print(trans_result)
