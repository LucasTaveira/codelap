from django.db import models

# Create your models here.
class Career(models.Model):
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id }, {self.username} : {self.title}'
    
