# Generated by Django 3.2.23 on 2023-11-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_app', '0002_auto_20231109_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='video_path',
            field=models.CharField(max_length=256, null=True),
        ),
    ]