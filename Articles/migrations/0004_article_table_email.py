# Generated by Django 3.2.13 on 2022-06-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_article_table_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_table',
            name='email',
            field=models.CharField(default=123, max_length=100),
        ),
    ]