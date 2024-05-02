# Generated by Django 5.0.3 on 2024-04-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_rename_login_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contct',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DriverDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('license', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
