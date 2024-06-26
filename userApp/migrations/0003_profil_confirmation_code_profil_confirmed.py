# Generated by Django 5.0.3 on 2024-03-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_profil_city_profil_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='confirmation_code',
            field=models.PositiveSmallIntegerField(default=111111),
        ),
        migrations.AddField(
            model_name='profil',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
