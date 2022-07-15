import profile
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) 


    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.author.username + self.title

















class UserProfileModel(models.Model):


    name = models.CharField(max_length=25)
    email = models.EmailField()
    pic = models.ImageField(upload_to='profile_pics')
    pdf = models.FileField(upload_to='resume')
    p_link = models.URLField()

    def __str__(self):

        return self.name + str(self.pk)

