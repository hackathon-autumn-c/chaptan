# Generated by Django 3.2.23 on 2023-11-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='status',
            field=models.CharField(default='処理中', max_length=50),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter_data',
            field=models.TextField(default='チャプター生成中'),
        ),
    ]
