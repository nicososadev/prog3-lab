# Generated by Django 3.1.2 on 2020-10-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='propiedad/', verbose_name='Imagen'),
        ),
    ]