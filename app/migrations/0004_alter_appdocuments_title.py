# Generated by Django 3.2 on 2022-01-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_appdocuments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdocuments',
            name='title',
            field=models.CharField(default='Restore', max_length=1000),
        ),
    ]
