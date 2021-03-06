# Generated by Django 3.2 on 2022-01-14 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220110_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StateIND',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=100)),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=256)),
                ('Gender', models.CharField(max_length=256)),
                ('DOB', models.CharField(max_length=256)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='StateID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind'),
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=256)),
                ('Gender', models.CharField(max_length=256)),
                ('DOB', models.CharField(max_length=256)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.AddField(
            model_name='cityvillage',
            name='TalukaID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka'),
        ),
    ]
