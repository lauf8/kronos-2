from django.urls import path

from post.views import post, PostCreateView, PostView, more_rating, less_rating, less_rating_post, more_rating_post

app_name = "post"


urlpatterns = [
    path('', post, name='post'),
    path('<int:routine>/create', PostCreateView.as_view(), name='post_create'),
    path('<int:post>',PostView.as_view(), name='post'),    
    path('<int:comment_id>/more',more_rating, name ='more_rating'),
    path('<int:comment_id>/less',less_rating, name ='less_rating'),
    path('<int:post_id>/post/less',less_rating_post, name ='less_rating_post'),
    path('<int:post_id>/post/more',more_rating_post, name ='more_rating_post'),
]
