# Generated by Django 4.2.7 on 2024-03-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaLink', '0004_bookmark_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user_id', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
