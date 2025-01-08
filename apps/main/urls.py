from django.urls import path
from apps.main.views import index, about_, contact


urlpatterns = [
    path('', index, name = 'index'),
    path('about.html', about_, name = 'about'),
    path("contact.html", contact, name="contact")

]
