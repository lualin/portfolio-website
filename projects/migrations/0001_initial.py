# Generated by Django 4.1.2 on 2023-05-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Projects',
            },
        ),
    ]
