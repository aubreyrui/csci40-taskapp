from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # one-to-one connection means you can't connect the profile to another user
    year_level = models.IntegerField()
    course = models.CharField(max_length = 10)

# Create your models here.
