from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.user}'

class Articles(models.Model):
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name="Article_Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tags")
    created_on = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.content
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Rooms(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name="Rooms_Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.name
    
    
    