# Generated by Django 4.1.2 on 2023-05-07 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='img_url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
