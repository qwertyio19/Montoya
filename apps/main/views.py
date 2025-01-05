from django.shortcuts import render
from apps.main.models import Main, Awards, About

# Create your views here.
def index(request):
    main = Main.objects.latest('id')
    return render(request, 'index.html', locals())


def about_(request_2):
    about = About.objects.latest("id")
    awards = Awards.objects.all()
    return render(request_2, 'about.html', locals())