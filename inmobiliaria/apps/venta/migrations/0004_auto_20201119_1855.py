# Generated by Django 3.1.2 on 2020-11-19 21:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_auto_20201103_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='created',
        ),
        migrations.AddField(
            model_name='venta',
            name='completed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Completada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='reserved',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Reservada'),
            preserve_default=False,
        ),
    ]