# Generated by Django 3.1.2 on 2020-12-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku_system', '0006_auto_20201214_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_mail',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lending_day',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_day',
            field=models.DateTimeField(),
        ),
    ]
