from django.urls import path
from apps.main.views import index, about_


urlpatterns = [
    path('', index, name = 'index'),
    path('about.html', about_, name = 'about')
]
