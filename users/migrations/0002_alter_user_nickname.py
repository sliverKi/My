# Generated by Django 4.1.7 on 2023-03-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
    ]