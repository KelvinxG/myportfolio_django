from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    object={'message':'Hello,world'}
    return render(request,'app/index.html')