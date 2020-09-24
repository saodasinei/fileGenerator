from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from DB import models
from . import generate
from django.core import serializers
import pandas as pd
import json
import datetime


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


