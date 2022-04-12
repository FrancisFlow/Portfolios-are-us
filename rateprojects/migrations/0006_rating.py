# Generated by Django 4.0.3 on 2022-04-12 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rateprojects', '0005_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('usability_rating', models.IntegerField(blank=True, default=0, null=True)),
                ('design_rating', models.IntegerField(blank=True, default=0, null=True)),
                ('content_rating', models.IntegerField(blank=True, default=0, null=True)),
                ('review', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rateprojects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]