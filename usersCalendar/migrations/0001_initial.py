# Generated by Django 4.1.7 on 2023-03-06 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(default='', max_length=150)),
                ('content', models.TextField(default='', max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersCalendar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': "User's Calendar",
            },
        ),
    ]
