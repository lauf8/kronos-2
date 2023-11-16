from django.urls import path

from post.views import post, PostView

app_name = "post"


urlpatterns = [
    path('', post, name='post'),
    path('<int:routine>/create', PostView.as_view(), name='post_create'),    
]
