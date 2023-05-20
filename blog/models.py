from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    
    STATUS_CHOICES = (
        ('pub', 'publish'),
        ('drf', 'draft')
    )

    title = models.CharField(max_length=160)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


    def __str__(self):
        return self.title