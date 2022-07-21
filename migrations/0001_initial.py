# Generated by Django 4.0 on 2022-01-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imgs')),
                ('area', models.TextField(max_length=20)),
                ('descr', models.TextField(max_length=100)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
