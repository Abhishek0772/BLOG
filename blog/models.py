from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200 ,unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now= True)
    category = models.CharField(max_length=100)
    images = models.ImageField(upload_to="media" , default='')

    def __str__(self):
        return self.title