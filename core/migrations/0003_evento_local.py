# Generated by Django 3.1.2 on 2020-10-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201024_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(default=1, max_length=130),
            preserve_default=False,
        ),
    ]
