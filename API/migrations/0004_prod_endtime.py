# Generated by Django 4.0 on 2021-12-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_remove_prod_endtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='endTime',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]