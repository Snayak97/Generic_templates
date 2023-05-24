from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse('<h1> this is my app2_string</h1>')


def app2_htmlpages(request):
    return render(request,'app2_htmlpages.html')
