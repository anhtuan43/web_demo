from django.db import models

# Create your models here.
class postForm(models.Model):
    title = models.CharField(max_length = 255)
    tag = models.CharField(max_length=100, default='general')
    image = models.ImageField(default='general')
    body = models.TextField()
    creates_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

