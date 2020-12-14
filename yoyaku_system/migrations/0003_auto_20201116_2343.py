# Generated by Django 3.1.2 on 2020-11-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku_system', '0002_auto_20201116_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=100)),
                ('equipment_number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='camera_manage',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='camera_manage',
            name='equipment_number',
        ),
    ]