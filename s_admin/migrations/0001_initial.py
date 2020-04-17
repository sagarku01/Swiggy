# Generated by Django 2.2.5 on 2020-04-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurenttypeModel',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('state_no', models.AutoField(primary_key=True, serialize=False)),
                ('State_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('city_no', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30, unique=True)),
                ('city_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.StateModel')),
            ],
        ),
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('area_no', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=30, unique=True)),
                ('area_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.CityModel')),
            ],
        ),
    ]
