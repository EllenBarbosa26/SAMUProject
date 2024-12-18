# Generated by Django 5.0.1 on 2024-11-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=64)),
                ('district', models.CharField(max_length=40)),
                ('number', models.IntegerField(null=True)),
                ('date_birth', models.DateField()),
                ('phone', models.CharField(max_length=15, null=True, unique=True)),
                ('cpf', models.CharField(max_length=11, null=True, unique=True)),
            ],
        ),
    ]
