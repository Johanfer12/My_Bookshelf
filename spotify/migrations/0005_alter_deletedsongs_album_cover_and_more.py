# Generated by Django 4.2.9 on 2025-01-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_deletedsongs_preview_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedsongs',
            name='album_cover',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deletedsongs',
            name='deleted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='deletedsongs',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='deletedsongs',
            name='preview_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
