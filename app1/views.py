from django.shortcuts import render

# Create your views here.
def display(request):
    dic1={'name':'ganesh'}
    res=render(request,"welcome.html",context=dic1)
    return res