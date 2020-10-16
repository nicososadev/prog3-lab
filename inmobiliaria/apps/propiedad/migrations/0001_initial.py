# Generated by Django 3.1.2 on 2020-10-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('propType', models.CharField(choices=[('CA', 'Casa'), ('DP', 'Departamento')], max_length=2)),
                ('operation', models.CharField(choices=[('AL', 'Alquiler'), ('VE', 'Venta')], max_length=2)),
                ('surfice', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
