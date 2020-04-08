from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    # return HttpResponse('This is sport index')
    return render(request, 'sport/index.html')
