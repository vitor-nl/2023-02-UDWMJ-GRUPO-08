# Generated by Django 4.1 on 2023-11-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
