# Generated by Django 3.1.2 on 2021-01-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user_ID',
            field=models.CharField(default='', max_length=100, verbose_name='ユーザーID'),
        ),
    ]
