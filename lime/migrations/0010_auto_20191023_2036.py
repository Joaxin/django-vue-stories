# Generated by Django 2.2.5 on 2019-10-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lime', '0009_auto_20191023_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.CharField(blank=True, default='mxh-cp-stories', max_length=200, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
