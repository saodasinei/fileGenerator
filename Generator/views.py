from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from DB import models
from . import generate
from django.core import serializers
import pandas as pd
import json


# Create your views here.
def generator(request):
    file = models.File.objects.all()
    profile = models.Profile.objects.all()
    return render(request, 'generator.html', {'files': file, 'profiles': profile})


def fission(request):
    if request.method == "POST":
        # print(request.body)
        # name = request.POST.get('name')
        # print("ok")
        # status = 1
        # result = "success"
        # import json
        # return HttpResponse(json.dumps({
        #     "status": status,
        #     "result": result,
        #     "name": name
        # }))
        print(request.body)
        data_post = request.body.decode("utf8")
        data = json.loads(data_post)
        files = generate.getfile(data[0])
        profiles = generate.getprofile(data[1])
        res = generate.generate(files, profiles)

        return HttpResponse(json.dumps(res))


def savenewfile(request):
    return HttpResponse("200")


def checking(file_list):
    for file in file_list:
        print(file)
    return HttpResponse(200)


import difflib


def equal(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def test(request):
    c = '#哥伦布献给了西班牙国王什么大宝贝？# 各位晚上好，这里是深夜一茄，我是王老六 相信各位在上一期已经猜的差不多了 这个历史事件呢，就是1492年，名垂青史的大航海家——哥伦布的闯入 这才让烟草这玩意，展现在了全世界人的面前 哥伦布发现烟草，也就是这个雪茄之后啊 回到了西班牙就把雪茄，当做稀世珍宝一样，献给了西班牙国王 而这西班牙国王啊，一看不错 人家又作为一个注重礼仪文化的王者， 就赋予了雪茄特别多的礼仪 之后呢，又经过百年的沉淀 这才渐渐形成了一套独特的品尝雪茄的方法 我们下期将会带各位了解雪茄的王者之路 有任何疑问可以私信我，记得把关注给我点了'
    a = '#雪茄的起源# 今天我们来讲一讲雪茄的起源 人类到底是什么时候开始抽烟的 估计现在基本上已经很难知晓了 其实根据现有的这样一个历史资料 我们只能知道最早开始会抽烟草的 是美洲大陆的原住民啊，就是土著人 也就是当时的玛雅人和印第安人 但是呢一件历史的重大事件把烟草推向了世界 下一期，带你详细了解烟草如何快速称霸世界'
    b = '#夜谈雪茄起源# 各位晚上好，这里是深夜一茄，我是王老六 今晚想和大家聊聊这个雪茄的起源 我们要想聊这个人类啊，到底是什么时候开始抽烟的 估计现在基本上也很难去弄清楚了 其实根据现有的这样一个历史资料 我们只能知道最早开始会抽烟草这玩意的 是美洲大陆的原住民，也就是土著人 像当时的玛雅人啊，印第安人啊 但是呢，发生一件重大的历史事件，这才把烟草推向了全世界 我们下期将会详细讲讲，烟草这玩意是如何快速称霸世界的 有任何疑问可以私信我，记得把关注给我点了'
    print(equal(c, b))
    return HttpResponse(200)
