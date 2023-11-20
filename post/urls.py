from django.urls import path

from post.views import post, PostCreateView, PostView

app_name = "post"


urlpatterns = [
    path('', post, name='post'),
    path('<int:routine>/create', PostCreateView.as_view(), name='post_create'),
    path('<int:post>',PostView.as_view(), name='post')    
]
