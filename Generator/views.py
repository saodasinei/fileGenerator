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
    profiles = excel_raw_data.iloc[1:2, :].values
    profile = {
            "series": profiles[0][1],
            "self": profiles[0][2],
            "fans": profiles[0][3],
            "greeting": profiles[0][4],
            "question": profiles[0][5],
            "praise": profiles[0][6],
            "tucao": profiles[0][7],
            "koupi1": profiles[0][8],
            "next": profiles[0][9],
            "end": profiles[0][10],
    }
    print(profile)
    fileid = excel_raw_data.iloc[5:, 0:1].values
    files = excel_raw_data.iloc[5:, 1:2].values
    newfiles = excel_raw_data.iloc[5:, 6:7].values
    file_list = []
    for i in range(len(fileid)):
        file = {"id": i+1, "file": files[i][0], "newfile": newfiles[i][0]}
        file_list.append(file)
    print(file_list)
    # print(fileid)
    # print(files)
    # print(newfiles)

    # return HttpResponse("200")
    return render(request, 'upload_checking.html', {"profile": profile, "files": file_list})


def history(request):
    return render(request, 'upload_history.html')


def search(request):
    file_id = request.GET.get("filedID")
    return HttpResponse(file_id)
