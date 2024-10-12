# Generated by Django 4.0 on 2024-10-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
