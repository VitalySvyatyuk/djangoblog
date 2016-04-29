from django.shortcuts import render
from django.http.response import HttpResponse

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is {} view.</body></html>".format(view)
    return HttpResponse(html)
