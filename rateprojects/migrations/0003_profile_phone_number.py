# Generated by Django 4.0.3 on 2022-04-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateprojects', '0002_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, default=123456789, max_length=14),
        ),
    ]
