# Generated by Django 3.1.5 on 2021-02-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstpage', '0003_auto_20210203_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
