from django.shortcuts import render

app_name = "post"


def post(request):
    return render(request, 'post/post.html')


def createPage(request):
    return render(request, 'post/create.html')
