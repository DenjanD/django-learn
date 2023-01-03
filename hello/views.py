from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
    classform = formss.classForm(request.POST or None)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/postindex/')

    
    context = {
        'heading':'Home',
        'classform': classform
    }
    return render(request, 'hello/forms.html', context)

def postindex(request):
    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }
    return render(request, 'hello/postindex.html',context)

def update(request, id):
    updt = Post.objects.get(id=id)
    data = {
        'title': updt.title,
        'body': updt.body,
    }
    classform = formss.classForm(request.POST or None, initial=data, instance=updt)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/postindex/')

    context = {
        'heading':'Updt',
        'classform': classform
    }
    return render(request, 'hello/forms.html', context)

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponseRedirect('/postindex/')
# def forms(request):
#     classform = formss.classForm()

#     context = {
#         'classform':classform,
#         'title':'',
#         'body':'',
#     }
#     if request.method == 'POST':
#         print("Ini method post")

#         Post.objects.create(
#             title = request.POST['title'],
#             body = request.POST['body']
#         )

#         context['title'] = request.POST['title']
#         context['body'] = request.POST['body']
#     else:
#         print("Ini method get")
#     return render(request, 'hello/forms.html', context)
