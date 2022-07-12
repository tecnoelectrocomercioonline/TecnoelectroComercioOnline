from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
import os

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)

    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer',
                                related_query_name='customer', null=True, blank=True)
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    image = models.ImageField(default='default/user.png')

    def __str__(self):
        # return "{} : {} []".format(self.user, self.username, self.first_name, self.last_name, self.phone) #ORIGINAL
        return str(self.user, self.username, self.first_name, self.last_name, self.phone)