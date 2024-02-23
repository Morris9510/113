from django.db import models
from django.urls import reverse


class Post(models.Model):                   #inheritance: Post extends Model
    title = models.CharField(max_length=128)        #composition: Post is composed of other classes
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])