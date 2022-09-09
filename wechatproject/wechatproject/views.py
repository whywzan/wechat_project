from django.http import HttpResponse
from django.shortcuts import render
import hashlib


def test_token(request):
    if request.method == 'GET':
        signature = request.GET["signature"]
        timestamp = request.GET["timestamp"]
        nonce = request.GET["nonce"]
        echostr = request.GET.get("echostr")
        token = "weixin"
        list = [token, timestamp, nonce]
        list.sort()
        hashstr = ''.join([s for s in list])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
    return HttpResponse("6666")