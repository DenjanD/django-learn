from django.shortcuts import render

def index(request):
    return render(request, 'hello/index.html')
    
def index2(request):
    return render(request, 'hello/index2child.html')