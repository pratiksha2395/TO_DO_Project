# Generated by Django 3.1.5 on 2021-02-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstpage', '0002_auto_20210202_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True),
        ),
    ]
