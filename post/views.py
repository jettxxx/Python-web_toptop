from traceback import print_tb
from turtle import pos
from django.http import HttpResponse
from django.shortcuts import render, redirect
from post.models import *
from .forms import post_Form

app_name = "post"


def post(request):
    auth_usr = request.user
    obj = Post.objects.all()
    context = {
        'usr': auth_usr,
        'obj': obj
    }
    return render(request, 'post/post.html', context)


def user_details(request, usr_id):
    auth_usr = request.user
    obj = Post.objects.filter(id=usr_id)
    context = {
        'usr': auth_usr,
        'obj': obj
    }
    return render(request, 'post/user_details.html', context)


def createPage(request):
    auth_usr = request.user
    pF = post_Form()
    context = {
        'usr': auth_usr,
        'pF': pF
    }
    return render(request, 'post/create.html', context)


def getPost(request):
    if request.method == "POST":
        pF = post_Form(request.POST, request.FILES)
        pF.instance.root_user = request.user
        if pF.is_valid():
            pF.save()
            mess = "Create Success!"
            context = {
                'mess': mess
            }
            return render(request, 'post/success.html', context)
    else:
        return HttpResponse("Wrong!")


def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')


def editPost(request, pk):
    p = Post.objects.get(id=pk)
    return render(request, 'post/edit.html', {'post': p})


def updatePost(request, pk):
    p = Post.objects.get(id=pk)
    if request.method == "POST":
        p.video_caption = request.POST['video_caption']
        p.video_url = request.POST['video_url']
        p.video_tag = request.POST['video_tag']
        p.save()
        return redirect('/')
