# Generated by Django 3.0 on 2020-01-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_auto_20200108_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]