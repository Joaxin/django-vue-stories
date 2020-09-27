# Generated by Django 2.2.5 on 2019-09-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lime', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='bookmark',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='valid'),
        ),
    ]