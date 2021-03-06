from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
    

class Catagory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    


class Post(models.Model):

    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=False)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey("Author",on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    catagories = models.ManyToManyField("Catagory")
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    

