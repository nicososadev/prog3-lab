# Generated by Django 3.1.2 on 2020-10-29 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('propiedad', '0003_auto_20201028_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='venta_agente', to=settings.AUTH_USER_MODEL)),
                ('propiedad', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='propiedad.propiedad')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='venta_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
