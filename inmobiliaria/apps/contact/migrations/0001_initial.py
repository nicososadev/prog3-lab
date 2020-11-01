# Generated by Django 3.1.2 on 2020-10-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('content', models.TextField(max_length=200, verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
