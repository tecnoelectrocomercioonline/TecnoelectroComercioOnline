from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.is_email_verified

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', related_query_name='customer', null=True, blank=True)
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(
        default="static/shop/img/profile1.png", null=True, blank=True)
        
    def __str__(self):
        return str(self.user, self.username, self.first_name, self.last_name, self.phone)
        # return "{} : {} []".format(self.user, self.username, self.first_name, self.last_name, self.phone) #ORIGINAL
        # return '{}, {}, {}, {}'.format(self.user, self.username, self.email, self.first_name, self.last_name, self.phone, self.profile_pic)
