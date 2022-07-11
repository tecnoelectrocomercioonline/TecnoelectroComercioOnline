from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

# class User(models.Model):
class User(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    # objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

#     is_email_verified = models.BooleanField(default=False)

#     def __str__(self):
#         # return self.is_email_verified
#         return str(self.is_email_verified)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer',
                                related_query_name='customer', null=True, blank=True)
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    profile_pic = models.ImageField(
        default="static/shop/img/profile1.png", null=True, blank=True)

    def __str__(self):
        # return "{} : {} []".format(self.user, self.username, self.first_name, self.last_name, self.phone) #ORIGINAL
        return str(self.user, self.username, self.first_name, self.last_name, self.phone)
