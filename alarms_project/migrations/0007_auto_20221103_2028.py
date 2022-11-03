# Generated by Django 2.1.11 on 2022-11-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms_project', '0006_auto_20221103_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmTone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.CharField(choices=[('music1', 'Love Story'), ('music2', 'Flower Dance'), ('music3', 'River Flows in You'), ('music4', 'Little Star')], default='music1', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Sound',
        ),
        migrations.RemoveField(
            model_name='alarm',
            name='sound',
        ),
    ]
