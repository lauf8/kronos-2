from django.urls import path

from post.views import post

app_name = "post"


urlpatterns = [
    path('', post, name='post'),    
]
