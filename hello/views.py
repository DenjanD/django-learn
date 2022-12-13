from django.shortcuts import render
from django.http import HttpResponse
from . import formss

from .models import Post

def index(request):

    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }
    return render(request, 'hello/index.html',context)
    
def index2(request):
    return render(request, 'hello/index2child.html')
    
def templateChallengeIndex(request):
    return render(request, 'hello/templatechallenge.html')

def articles(request,year):
    year=year
    str=year
    return HttpResponse(year)

def forms(request):
    classform = formss.classForm()

    context = {
        'classform':classform,
        'title':'',
        'body':'',
    }
    if request.method == 'POST':
        print("Ini method post")

        Post.objects.create(
            title = request.POST['title'],
            body = request.POST['body']
        )

        context['title'] = request.POST['title']
        context['body'] = request.POST['body']
    else:
        print("Ini method get")
    return render(request, 'hello/forms.html', context)
