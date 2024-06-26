# Generated by Django 3.0 on 2020-01-08 13:26

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
            name='ParentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Pst', 'Pastor'), ('Dr', 'Dr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Rev', 'Rev'), ('Miss', 'Miss')], max_length=15)),
                ('surname', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('profile_piture', models.ImageField(blank=True, null=True, upload_to='img/parent')),
                ('first_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('state_of_origin', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male')], max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
