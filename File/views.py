from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from DB import models
from django.core import serializers
import pandas as pd
import json
import datetime


# Create your views here.
def login(request):
    return render(request, 'login.html')


def identify(request):
    print(request.body)
    return HttpResponse("200")


def upload(request):
    return render(request, 'upload.html')


def uploadexcel(request):
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    profiles = excel_raw_data.iloc[1:2, :].values
    profile = {
        "number": profiles[0][0],
        "series": profiles[0][1],
        "self": profiles[0][2],
        "fans": profiles[0][3],
        "greeting": profiles[0][4],
        "question": profiles[0][5],
        "praise": profiles[0][6],
        "tucao": profiles[0][7],
        "koupi": profiles[0][8],
        "next": profiles[0][9],
        "end": profiles[0][10],
    }
    # print(profile)
    fileid = excel_raw_data.iloc[5:, 0:1].values
    files = excel_raw_data.iloc[5:, 1:2].values
    newfiles = excel_raw_data.iloc[5:, 6:7].values
    file_list = []
    for i in range(len(fileid)):
        file = {"id": i + 1, "file": files[i][0], "newfile": newfiles[i][0]}
        file_list.append(file)
    # print(file_list)
    # print(fileid)
    # print(files)
    # print(newfiles)
    # return HttpResponse("200")
    return render(request, 'upload_checking.html', {"profile": profile, "files": file_list})


def saveupload(request):
    if request.method == "POST":
        data_post = request.body.decode("utf8")
        data = json.loads(data_post)
        profile_mumber = data[0]
        files = data[1:]

        print(profile_mumber)
        print(files)

        time = datetime.datetime.now()
        now = time + datetime.timedelta(hours=8)
        print(now)
        d1 = models.PartTimer.objects.get(id=1)
        d2 = models.Profile.objects.get(number=profile_mumber)
        uploadlist = models.UploadList(parttimer_id=d1, profile_id=d2, createdate=now)
        uploadlist.save()

        print(uploadlist.id)
        d3 = models.UploadList.objects.get(id=uploadlist.id)

        for file in files:
            d4 = models.File.objects.get(id=file[0])
            uploadfile = models.UploadFile(upload_id=d3, template_id=d4, content=file[1])
            uploadfile.save()

    return HttpResponse("200")


def history(request):
    uploadlist = models.UploadList.objects.all()

    return render(request, 'upload_history.html', {"uploadlist": uploadlist})


def content(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        content = models.UploadFile.objects.filter(upload_id=id).values()
        data = list(content)
        print(data)
        # data = serializers.serialize('json', content)
        # data = json.dumps(data)
        # print(data)
        # print(request.body)
    return HttpResponse(json.dumps(data))


def manage(request):
    return render(request, 'manage.html')


def search(request):
    file_id = request.GET.get("filedID")
    return HttpResponse(file_id)
