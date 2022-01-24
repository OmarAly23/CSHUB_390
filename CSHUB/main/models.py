from django.db import models

# Create your models here.
# each model maps to a database table

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10, default='null')
    last_name = models.CharField(max_length=10, default='null')
    email = models.EmailField(max_length=30, help_text="Enter your email: ")
    password = models.CharField(max_length=23, help_text="Enter your password: ")
    resource_history = models.CharField(max_length=100)
    resources_added = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.email

class Resource(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, default="general")
    title = models.CharField(max_length=100, default="general")
    description = models.CharField(max_length=255, default="general")

    objects = models.Manager()

    def __int__(self):
        return self.resource_id
