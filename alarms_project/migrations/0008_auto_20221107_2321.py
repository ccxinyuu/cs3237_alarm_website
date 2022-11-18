# Generated by Django 2.1.11 on 2022-11-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarms_project', '0007_auto_20221103_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datetime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='alarmtone',
            name='sound',
            field=models.CharField(choices=[('Love Story', 'Love Story'), ('Flower Dance', 'Flower Dance'), ('River Flows in You', 'River Flows in You'), ('Little Star', 'Little Star')], default='Love Story', max_length=200),
        ),
    ]