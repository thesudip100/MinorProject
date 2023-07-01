# Generated by Django 4.2.2 on 2023-06-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('fullAddress', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('profilePic', models.ImageField(upload_to='customers_pic/')),
            ],
        ),
    ]