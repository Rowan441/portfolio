# Generated by Django 3.2 on 2021-05-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210504_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='jobs.Topic'),
        ),
    ]
