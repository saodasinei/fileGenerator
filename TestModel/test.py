from django.test import TestCase
from django.http import HttpResponse
import json


# Create your tests here.
def testPost(request):
    if request.method == "POST":
        data_post = request.body.decode("utf8")
        data = json.loads(data_post)
        print(data)
        return HttpResponse(200)
    else:
        return HttpResponse(500)