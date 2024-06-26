# Generated by Django 4.2.7 on 2024-02-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaLink', '0002_like_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='cmnt_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField()),
                ('content', models.TextField()),
                ('user_id', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
