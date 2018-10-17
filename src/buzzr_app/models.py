from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharFIeld(max_length=100)
    follwers = models.IntegerField()
    join_date = models.DateField()


class Buzz(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    num_likes = models.IntegerField()

    def __str__(self):
        return self.title
