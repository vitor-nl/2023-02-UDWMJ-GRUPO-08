from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('User', max_length=100)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering =['id']

    def __str__(self):
        return self.name