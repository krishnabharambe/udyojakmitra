# Generated by Django 3.2 on 2022-01-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220114_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityvillage',
            name='Status',
            field=models.CharField(default='Inactive', max_length=100),
        ),
        migrations.AddField(
            model_name='district',
            name='Status',
            field=models.CharField(default='Inactive', max_length=100),
        ),
        migrations.AddField(
            model_name='stateind',
            name='Status',
            field=models.CharField(default='Inactive', max_length=100),
        ),
        migrations.AddField(
            model_name='taluka',
            name='Status',
            field=models.CharField(default='Inactive', max_length=100),
        ),
    ]
