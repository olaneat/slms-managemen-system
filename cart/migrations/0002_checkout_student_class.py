# Generated by Django 3.0 on 2020-01-07 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='student_class',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.StudentClass'),
        ),
    ]
