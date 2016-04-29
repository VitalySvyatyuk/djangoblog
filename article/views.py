from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is {} view.</body></html>".format(view)
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render({'name': view})
    return HttpResponse(html)

def template_three_simple(request):
    view = "template three simple"
    return render_to_response('myview.html', {'name': view})
