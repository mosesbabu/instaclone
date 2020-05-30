from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
  url(r'^feed/',views.newsfeed,name='Home'),
  url(r'^$',views.signup,name='SignUp'),
  url(r'^newsfeed_images/',views.newsfeed_images,name='images'),
  url(r'^profile/',views.profile,name='Profile'),
  url(r'^about_me/',views.profile_about,name='about'),
 
]