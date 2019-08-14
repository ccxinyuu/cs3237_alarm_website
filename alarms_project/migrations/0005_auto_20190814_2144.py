# Generated by Django 2.1 on 2019-08-14 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alarms_project', '0004_auto_20190813_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='sound',
            field=models.ForeignKey(default=1, help_text='Choose the sound for your alarm', on_delete=django.db.models.deletion.CASCADE, to='alarms_project.Sound'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='time',
            field=models.DateTimeField(help_text='Choose a date and time for your alarm that is BEFORE the current time'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='title',
            field=models.CharField(default='Alarm', help_text='Enter a nice name for the alarm', max_length=200),
        ),
    ]