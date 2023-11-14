from django.db import models
from accounts.models.user import User
from routine.models import Routine
class Post(models.Model):  
    title = models.CharField(max_length=150)
    text = models.TextField()
    rating = models.IntegerField()
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()

