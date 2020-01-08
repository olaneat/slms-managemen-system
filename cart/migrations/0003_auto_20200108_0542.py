# Generated by Django 3.0 on 2020-01-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_checkout_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='student_class',
            field=models.CharField(choices=[('JSS 1A', 'JSS 1A'), ('JSS 1B', 'JSS 1B'), ('JSS 1C', 'JSS 1C'), ('JSS 2A', 'JSS 2A'), ('JSS 2B', 'JSS 2B'), ('JSS 2C', 'JSS 2C'), ('JSS 3A', 'JSS 3A'), ('JSS 3B', 'JSS 3B'), ('JSS 3C', 'JSS 3C'), ('SS 1A', 'SS 1A'), ('SS 1B', 'SS 1B'), ('SS 1C', 'SS 1C'), ('SS 2A', 'SS 2A'), ('SS 2B', 'SS 2B'), ('SS 2C', 'SS 2C'), ('SS 3A', 'SS 3A'), ('SS 3B', 'SS 3B'), ('SS 3C', 'SS 3C')], max_length=15),
        ),
    ]
