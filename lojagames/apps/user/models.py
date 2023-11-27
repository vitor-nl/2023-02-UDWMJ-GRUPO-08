from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField('Data de nascimento',)
    password = models.CharField('Senha', max_length=20)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering =['id']

    def __str__(self):
        return self.first_name