# from django.db import models
# from django.contrib.auth.models import User, AbstractUser
# from shop.models import Customer
# import os

# class Customer(models.Model):
#     # user = models.OneToOneField(default='user' , on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=25, null=True)
#     username = models.CharField(max_length=50, null=True)
#     email = models.CharField(max_length=50, null=True)
#     phone = models.CharField(max_length=25, null=True)
#     address = models.TextField("Direccion", max_length=600, default='', blank=True)
#     date_created = models.DateTimeField(
#         auto_now_add=True, null=True, blank=True)
#     # image = models.ImageField(default='default/user.png')

#     def __str__(self):
#         # return "{} : {} []".format(self.user, self.username, self.first_name, self.last_name, self.phone) #ORIGINAL
#         return str(self.user, self.username, self.first_name, self.last_name, self.phone, self.email, self.address)

# class CustomUser(User):
#     def image_upload_to(self, instance=None):
#         if instance:
#             return os.path.join("Users", self.username, instance)
#         return None

#     STATUS = (
#         ('regular', 'regular'),
#         ('subscriber', 'subscriber'),
#         ('moderator', 'moderator'),
#     )
#     image = models.ImageField(
#         default='default/user.png', upload_to=image_upload_to)
#     address = models.TextField("Direccion", max_length=600, default='', blank=True)
#     description = models.TextField(
#         "Description", max_length=600, default='', blank=True)
#     date_created = models.DateTimeField(
#         auto_now_add=True, null=True, blank=True)
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer',
#                                     related_query_name='customer', null=True, blank=True)
#     status = models.CharField(
#         max_length=100, choices=STATUS, default='regular')

#     def __str__(self):
#         return self.username
