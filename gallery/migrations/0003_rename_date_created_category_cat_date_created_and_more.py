# Generated by Django 4.1.2 on 2022-10-28 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='date_created',
            new_name='cat_date_created',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='last_updated',
            new_name='cat_last_updated',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='cat_slug',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='cat_title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='uniqueID',
            new_name='cat_uniqueID',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='altText',
            new_name='img_altText',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='description',
            new_name='img_description',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='hashtags',
            new_name='img_hashtags',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='slug',
            new_name='img_slug',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='uniqueId',
            new_name='img_uniqueId',
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='image',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='image',
            name='img_date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='img_last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(blank=True, max_length=200, null=True)),
                ('album_description', models.TextField(blank=True, null=True)),
                ('album_uniqueID', models.CharField(blank=True, max_length=100, null=True)),
                ('album_active', models.BooleanField()),
                ('album_date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('album_date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.album'),
        ),
    ]