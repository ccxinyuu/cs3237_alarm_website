# Generated by Django 2.1.11 on 2022-11-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms_project', '0005_auto_20190814_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sound',
            name='audio',
        ),
        migrations.AlterField(
            model_name='alarm',
            name='sound',
            field=models.CharField(choices=[('music1', 'Love Story'), ('music2', 'Flower Dance'), ('music3', 'River Flows in You'), ('music4', 'Little Star')], default='music1', max_length=200),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='time',
            field=models.DateTimeField(help_text='Choose a date and time for your alarm that is AFTER the current time'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='title',
            field=models.CharField(default='Alarm', help_text='Enter the name for your alarm', max_length=200),
        ),
        migrations.AlterField(
            model_name='sound',
            name='name',
            field=models.CharField(choices=[('music1', 'GREEN'), ('music2', 'BLUE'), ('music3', 'RED'), ('music4', 'ORANGE')], default='music1', max_length=200),
        ),
    ]
