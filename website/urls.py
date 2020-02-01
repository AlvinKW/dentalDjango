from django.urls import path
from . import views #from this website directory import views files

urlpatterns = [ #handles different urls
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
]
