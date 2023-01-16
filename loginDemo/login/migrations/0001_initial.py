# Generated by Django 4.1.5 on 2023-01-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    #执行python3 manage.py makemigrations创建的数据库语句
    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]
