# Generated by Django 4.0.6 on 2022-07-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_news_tags_news_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.tag'),
        ),
    ]
