from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators import csrf
from DB import models
from Generator.views import checking
import pandas as pd
import json
import difflib
import datetime


# Create your views here.
def loginValid(fun):
    def inner(request, *args, **kwargs):
        session = request.session.get('username')
        if session:
            user = models.PartTimer.objects.filter(username=session).first()
            if user:
                return fun(request, *args, **kwargs)
            else:
                return redirect('/file/login/')
        else:
            return redirect('/file/login/')

    return inner


# login
@loginValid
def index(request):
    return render(request, 'index.html')


# def index(request):
#     username = request.session.get('username', '')
#     if not username:
#         return redirect('/file/login/')
#     return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


# 登陆
def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']

    user = models.PartTimer.objects.filter(username=username, password=password)
    if user:
        id = list(user.values_list('id', flat=True))[0]
        request.session['username'] = username
        request.session['userid'] = id
        return render(request, 'index.html')
    else:
        return HttpResponse("你输入的账号或密码有误！")
    # result = models.PartTimer.objects.filter(username=username, password=password).count()
    #
    # if result == 1:
    #     request.session['username'] = username
    #     return render(request, 'upload.html')
    # else:
    #     return HttpResponse("你输入的账号或密码有误!")


# 注销
def logoutAction(request):
    logout(request)
    return redirect("/file/")


# fileupload
@loginValid
def upload(request):
    return render(request, 'upload.html')


def equal(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def checking(file_list):
    results = []
    rates = []
    checkingFiles = models.UploadFile.objects.all().values()
    checkingFilesList = list(checkingFiles)
    # print(checkingFilesList)
    for file in file_list:
        # print(file['newfile'])
        rate = []
        for checkingFile in checkingFilesList:
            if file['id'] == checkingFile['template_id_id']:
                # print(checkingFile['content'])
                result = equal(file['newfile'], checkingFile['content'])
                # print(result)
                rate.append(result)
                # print(rate)
                results.append({'id': file['id'], 'upload_id': checkingFile['upload_id_id'], 'rate': result})
        # print(sum(rate)/len(rate))
        rates.append(sum(rate) / len(rate))
    # print(sum(rates) / len(rates))
    total_rate = round(sum(rates) / len(rates), 4) * 100
    print(total_rate)
    # results.append({'total_rate': total_rate})
    return total_rate


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
    rate = checking(file_list)
    # print(file_list)
    # print(fileid)
    # print(files)
    # print(newfiles)
    # return HttpResponse("200")
    return render(request, 'upload_text.html', {"profile": profile, "files": file_list, 'rate': rate})


@loginValid
def saveupload(request):
    if request.method == "POST":
        data_post = request.body.decode("utf8")
        data = json.loads(data_post)
        profile_number = data[0]
        files = data[1:]

        # print(profile_number)
        # print(files)

        # time = datetime.datetime.now()
        # now = time + datetime.timedelta(hours=8)
        # print(now)
        parttimerId = request.session.get('userid')
        d1 = models.PartTimer.objects.get(id=parttimerId)
        d2 = models.Profile.objects.get(number=profile_number)
        uploadList = models.UploadList(parttimer_id=d1, profile_id=d2)
        uploadList.save()

        # print(uploadList.id)
        d3 = models.UploadList.objects.get(id=uploadList.id)

        for file in files:
            d4 = models.File.objects.get(id=file[0])
            uploadfile = models.UploadFile(upload_id=d3, template_id=d4, content=file[1])
            uploadfile.save()

    return HttpResponse("200")


# uploadHistory
@loginValid
def history(request):
    id = request.session.get('userid')
    uploadlist = models.UploadList.objects.filter(parttimer_id=id)
    return render(request, 'upload_history.html', {"uploadlist": uploadlist})


@loginValid
# def content(request):
#     if request.method == 'GET':
#         id = request.GET.get("id")
#         content = models.UploadFile.objects.filter(upload_id=id)
#         print(content)
#     return render(request, 'history_content.html', {'content': content})

def content(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        content = models.UploadFile.objects.filter(upload_id=id).values()
        data = list(content)
        print(data)
        files = []
        for file in data:
            print(file['content'])
            file['content'].replace(' ', '\n')
            files.append(file)
            print(file)
        print(files)
    return render(request, 'history_content.html', {'content': files})


@loginValid
def delete(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        models.UploadFile.objects.filter(upload_id=id).delete()
        models.UploadList.objects.filter(id=id).delete()
    return HttpResponse(200)


def managerLogin(request):
    return render(request, 'manage_login.html')


def manage(request):
    return render(request, 'manage.html', )


def manageReview(request):
    partTimer = models.PartTimer.objects.all()
    historyList = models.UploadList.objects.all()
    return render(request, 'manage_review.html', {'partTimer': partTimer, 'historyList': historyList})


def reviewFilter(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        if id:
            partTimer = models.PartTimer.objects.all()
            historyList = models.UploadList.objects.filter(parttimer_id=id)
        else:
            partTimer = models.PartTimer.objects.all()
            historyList = models.UploadList.objects.all()
    return render(request, 'manage_review.html', {'partTimer': partTimer, 'historyList': historyList})


def reviewContent(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        profileId = request.GET.get("profile")
        content = models.UploadFile.objects.filter(upload_id=id)
        profile = models.Profile.objects.filter(series=profileId).values()
        # print(id)
        # print(profileId)
        # print(content)
        # print(list(profile)[0])
    return render(request, 'manage_review_content.html', {'content': content, 'profile': list(profile)[0]})


def uploadStatus(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        status = request.GET.get('status')
        models.UploadList.objects.filter(id=id).update(status=status)
        return HttpResponse(200)


def contentStatus(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        status = request.GET.get('status')
        models.UploadFile.objects.filter(id=id).update(status=status)
    return HttpResponse(200)


def manageParttimer(request):
    parttimer = models.PartTimer.objects.all()
    return render(request, 'manage_parttimer.html', {'parttimer': parttimer})


def addParttimer(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')
    user = models.PartTimer.objects.filter(username=username)
    if user:
        return HttpResponse('用户已存在')
    else:
        parttimer = models.PartTimer(username=username, password=password, name=name)
        parttimer.save()
        return HttpResponse('添加成功')


def updateParttimer(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')
    print(username)
    print(password)
    print(name)
    models.PartTimer.objects.filter(username=username).update(password=password, name=name)
    return HttpResponse('修改成功')


def deleteParttimer(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(id)
        models.PartTimer.objects.filter(id=id).delete()
    return HttpResponse(200)


def search(request):
    file_id = request.GET.get("filedID")
    return HttpResponse(file_id)
