from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


def runoob(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'runoob.html', context)
