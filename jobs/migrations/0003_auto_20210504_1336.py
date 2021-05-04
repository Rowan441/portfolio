# Generated by Django 3.2 on 2021-05-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210422_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='topics',
            field=models.ManyToManyField(blank=True, to='jobs.Topic'),
        ),
    ]
