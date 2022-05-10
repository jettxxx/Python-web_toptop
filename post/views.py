from django.http import HttpResponse
from django.shortcuts import render
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
