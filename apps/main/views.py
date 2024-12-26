from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def about_(request_2):
    return render(request_2, 'about.html', locals())