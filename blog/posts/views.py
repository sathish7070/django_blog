from django.shortcuts import render
from .models import posts

# Create your views here.

def index (request):
    post=posts.objects.all()
    return render (request,'index.html',{'post':post})

def post(request,pk):
    posts=post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})
