# Generated by Django 2.2.5 on 2019-11-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_main', '0003_auto_20191104_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
        migrations.AddField(
            model_name='profile',
            name='liked_answers',
            field=models.ManyToManyField(blank=True, related_name='users_liked', to='QA_main.Answer', verbose_name='Liked answers'),
        ),
        migrations.AddField(
            model_name='profile',
            name='liked_questions',
            field=models.ManyToManyField(blank=True, related_name='users_liked', to='QA_main.Question', verbose_name='Liked questions'),
        ),
    ]
