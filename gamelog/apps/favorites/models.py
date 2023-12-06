from django.db import models
from user.models import User

# Create your models here.

class Favorites(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    review_name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    release_date = models.DateField('Data de Lançamento', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Favorites'
        ordering =['id']

    def __str__(self):
        return self.name