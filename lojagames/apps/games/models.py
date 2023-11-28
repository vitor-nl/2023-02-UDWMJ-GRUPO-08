from django.db import models

# Create your models here.

class Games(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    review = models.CharField('Review', max_length=500) 
    note = models.IntegerField('Nota')
    release_date = models.DateField('Data de Lançamento', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Games'
        ordering =['id']

    def __str__(self):
        return self.name