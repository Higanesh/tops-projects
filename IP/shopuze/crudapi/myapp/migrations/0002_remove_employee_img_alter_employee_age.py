# Generated by Django 5.2.1 on 2025-05-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='img',
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(max_length=20),
        ),
    ]
