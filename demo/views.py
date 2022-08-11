from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def fraud(request):
    return render(request,'fraud.html')

def learn(request):
    return render(request,'learn.html')


def vote(request):
    return render(request,'vote.html')
