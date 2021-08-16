from django.http import request
from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'app.html',context={'name':'manu','age':3})



def hello(request):
    return render(request,'app1.html',context={'name':'manu','age':3})
    




