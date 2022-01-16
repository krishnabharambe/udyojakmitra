# Generated by Django 3.2 on 2022-01-16 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_homeimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='address',
            new_name='Address',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='contact',
        ),
        migrations.AddField(
            model_name='worker',
            name='AadharNo',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Ans1',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Ans2',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Ans3',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Ans4',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Ans5',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='BusinessName',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Contact',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='IFSC_Branch',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='IFSC_Code',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='PanNo',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Que1',
            field=models.CharField(default='Since how long are you doing this work?', max_length=1000),
        ),
        migrations.AddField(
            model_name='worker',
            name='Que2',
            field=models.CharField(default='what is your annual turnover?', max_length=1000),
        ),
        migrations.AddField(
            model_name='worker',
            name='Que3',
            field=models.CharField(default='Do you do cashless transactions?', max_length=1000),
        ),
        migrations.AddField(
            model_name='worker',
            name='Que4',
            field=models.CharField(default='Are you wiling to take a contract? what is the maximum contract amount?', max_length=1000),
        ),
        migrations.AddField(
            model_name='worker',
            name='Que5',
            field=models.CharField(default='How early can you serve the customer after receiving a call or message?', max_length=1000),
        ),
        migrations.AddField(
            model_name='worker',
            name='WorkType',
            field=models.CharField(default=11, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='accountHolderName',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='accountNo',
            field=models.CharField(default=11, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='fullname',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='WorkerLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('BusinessName', models.CharField(max_length=1000)),
                ('WorkType', models.CharField(max_length=1000)),
                ('AadharNo', models.CharField(max_length=1000)),
                ('PanNo', models.CharField(max_length=1000)),
                ('Contact', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('Address', models.TextField()),
                ('accountHolderName', models.CharField(max_length=1000)),
                ('accountNo', models.CharField(max_length=250)),
                ('IFSC_Code', models.CharField(max_length=250)),
                ('IFSC_Branch', models.CharField(max_length=250)),
                ('Que1', models.CharField(default='', max_length=1000)),
                ('Ans1', models.CharField(max_length=1000)),
                ('Que2', models.CharField(max_length=1000)),
                ('Ans2', models.CharField(max_length=1000)),
                ('Que3', models.CharField(max_length=1000)),
                ('Ans3', models.CharField(max_length=1000)),
                ('Que4', models.CharField(max_length=1000)),
                ('Ans4', models.CharField(max_length=1000)),
                ('Que5', models.CharField(max_length=1000)),
                ('Ans5', models.CharField(max_length=1000)),
                ('Que6', models.CharField(max_length=1000)),
                ('Ans6', models.CharField(max_length=1000)),
                ('Que7', models.CharField(max_length=1000)),
                ('Ans7', models.CharField(max_length=1000)),
                ('Que8', models.CharField(max_length=1000)),
                ('Ans8', models.CharField(max_length=1000)),
                ('Que9', models.CharField(max_length=1000)),
                ('Ans9', models.CharField(max_length=1000)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='TalukaHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('AadharNo', models.CharField(max_length=1000)),
                ('PanNo', models.CharField(max_length=1000)),
                ('Contact', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('profilepic', models.ImageField(upload_to='TalukaHandler/')),
                ('Address', models.TextField()),
                ('accountHolderName', models.CharField(max_length=1000)),
                ('accountNo', models.CharField(max_length=250)),
                ('IFSC_Code', models.CharField(max_length=250)),
                ('IFSC_Branch', models.CharField(max_length=250)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='M_Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('AadharNo', models.CharField(max_length=1000)),
                ('PanNo', models.CharField(max_length=1000)),
                ('Contact', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('profilepic', models.ImageField(upload_to='M_Operator/')),
                ('Address', models.TextField()),
                ('accountHolderName', models.CharField(max_length=1000)),
                ('accountNo', models.CharField(max_length=250)),
                ('IFSC_Code', models.CharField(max_length=250)),
                ('IFSC_Branch', models.CharField(max_length=250)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('AadharNo', models.CharField(max_length=1000)),
                ('PanNo', models.CharField(max_length=1000)),
                ('Contact', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('Address', models.TextField()),
                ('profilepic', models.ImageField(upload_to='DistrictHandler/')),
                ('accountHolderName', models.CharField(max_length=1000)),
                ('accountNo', models.CharField(max_length=250)),
                ('IFSC_Code', models.CharField(max_length=250)),
                ('IFSC_Branch', models.CharField(max_length=250)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('BusinessName', models.CharField(max_length=1000)),
                ('WorkType', models.CharField(max_length=1000)),
                ('AadharNo', models.CharField(max_length=1000)),
                ('PanNo', models.CharField(max_length=1000)),
                ('Contact', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('Address', models.TextField()),
                ('accountHolderName', models.CharField(max_length=1000)),
                ('accountNo', models.CharField(max_length=250)),
                ('IFSC_Code', models.CharField(max_length=250)),
                ('IFSC_Branch', models.CharField(max_length=250)),
                ('CityVillageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cityvillage')),
                ('DistrictID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('StateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stateind')),
                ('TalukaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.taluka')),
            ],
        ),
    ]
