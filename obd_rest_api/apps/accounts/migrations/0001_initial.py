# Generated by Django 4.0.4 on 2022-04-13 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
                ('construction_year', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('benzin', 'benzin'), ('diesel', 'diesel')], default='benzin', max_length=6)),
                ('mass_kg', models.IntegerField()),
                ('engine_displacement_l', models.FloatField()),
                ('number_of_cylinders', models.IntegerField()),
                ('milage_km', models.IntegerField()),
                ('power_ps', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('driving_license_since', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('diverse', 'diverse')], default='male', max_length=7)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='account', to='accounts.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
