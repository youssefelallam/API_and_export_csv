# Generated by Django 4.0 on 2021-12-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='endTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='prod',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]