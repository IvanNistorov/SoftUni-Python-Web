# Generated by Django 4.1.2 on 2022-10-30 07:58

import django.core.validators
from django.db import migrations, models
import django_basics_exam.cars.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('car_model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField(validators=[django_basics_exam.cars.models.year_validation])),
                ('image', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django_basics_exam.cars.models.min_length_validator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
