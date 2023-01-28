# Generated by Django 2.1.7 on 2023-01-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20230127_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'To do'), (1, 'Doing'), (2, 'Done')], default=0),
        ),
    ]
