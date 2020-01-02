# Generated by Django 3.0 on 2020-01-02 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('body', models.TextField()),
                ('author', models.CharField(blank=True, max_length=120, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='img/blog')),
                ('created', models.DateField()),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
