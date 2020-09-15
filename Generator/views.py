from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from DB import models
from . import generate
import pandas as pd


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
        import json
        print(request.body)
        data_post = request.body.decode("utf8")
        data = json.loads(data_post)
        files = generate.getfile(data[0])
        profiles = generate.getprofile(data[1])
        res = generate.generate(files, profiles)

        return HttpResponse(json.dumps(res))


def savenewfile(request):
    return HttpResponse("200")


def upload(request):
    return render(request, 'upload.html')


def uploadexcel(request):
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    print(excel_raw_data)
    return HttpResponse("200")


def search(request):
    file_id = request.GET.get("filedID")
    return HttpResponse(file_id)
