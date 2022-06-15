# Generated by Django 4.0.4 on 2022-06-13 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raspberry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry',
            name='used_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='used_raspberries', to=settings.AUTH_USER_MODEL),
        ),
    ]