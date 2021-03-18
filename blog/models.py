from django.conf import settings
from django.db import models
from django.utils import timezone

# creating a model for the post which content author, content ,publishing date
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    title= models.CharField(max_length= 2090)
    text = models.TextField()
    created_date = models.DateTimeField(timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
       
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title