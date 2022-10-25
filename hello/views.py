from django.shortcuts import render

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