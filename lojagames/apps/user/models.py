from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser): 
    username = models.CharField('Nome', max_length=100,unique=True)
    email = models.EmailField('E-mail',null=False, blank=False,unique=True)
    password = models.CharField('Senha', max_length=100)


    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering =['id']

    def __str__(self):
        return self.username