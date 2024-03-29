from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class User_M(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User_p')
    adress = models.TextField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=13, blank=True, default='')
    AboutMe = models.TextField(max_length=256, blank=True, default='')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class User_photo(models.Model):
    user = models.ForeignKey(User_M, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Chat(models.Model):
    members = models.ManyToManyField(User)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='A')
    message = models.TextField(max_length=256)

    def __str__(self):
        return self.message
