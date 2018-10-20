from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharFIeld(max_length=100)
    followers = models.IntegerField(default=0)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Buzz(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
