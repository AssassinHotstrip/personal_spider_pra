# coding:utf-8

import chardet
import requests

from ..http.response import Response


class Downloader(object):
    """框架提供的下载器, 接受引擎发来的请求,并返回响应给引擎"""

    def send_request(self, request):
        if request.method.upper() == "GET":
            response = requests.get(url=request.url, headers=request.headers, params=request.params, proxies=request.proxy)
        elif request.method.upper() == "POST":
            response = requests.post(url=request.url, headers=request.headers, formdata=request.formdata, proxies=request.proxy)
        else:
            raise TypeError("Not support request method :[{}]".format(request.method))

        return Response(url=response.url, headers=response.headers, body=response.content, status=response.status_code, encoding=chardet.detect(response.content)["encoding"])
        # >>>[In]: chardet.detect(response.content)
        # >>>[Out]: {"confidence": 0.99, "encoding" : "utf-8", "language" : ""}


