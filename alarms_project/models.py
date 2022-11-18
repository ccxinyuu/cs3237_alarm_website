from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from rules.contrib.models import RulesModel
import rules
# from datetime import datetime
import datetime
from pytz import UTC
import pickle

import os
from django.conf import settings

file_alarm_prediction = os.path.join(settings.BASE_DIR, 'alarm_prediction_alarm.sav')


@rules.predicate
def is_alarm_creator(user, alarm):
    return alarm.creator == user


rules.add_rule('can_edit_alarm', is_alarm_creator)
rules.add_perm('alarm.edit_alarm', is_alarm_creator)


# Create your models here.
class AlarmManager(models.Manager):
    def create_alarm(self, user):
        # load model
        loaded_model_predict_time = pickle.load(open(file_alarm_prediction, 'rb'))
        now = datetime.datetime.now()
        # get the weekday info 
        week_day = now.weekday()
        # feed in machine learning model 
        result = loaded_model_predict_time.predict([[0, week_day]])
        hour, minute = 0, 0
        num_min = int(result[0])
        if result[0] < 0:
            hour = (num_min + 1440) // 60 
            minute = (num_min + 1440 ) % 60 
        else:
            hour = num_min // 60 
            minute = num_min % 60
            
        now = datetime.datetime.now()
        tzinfo = datetime.timezone(datetime.timedelta(hours=4, minutes=0))
        new_time = datetime.datetime(now.year, now.month, now.day + 1, hour, minute, tzinfo=tzinfo)
        print(new_time)
        alarm = self.create(title="Alarm_Predict", creator=user, time=new_time)
        return alarm


class Alarm(RulesModel):
    """Model representing an alarm"""
    title = models.CharField(max_length=200, default='Alarm', help_text='Enter the name for your alarm')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # sound = models.CharField(max_length=200, choices = ALARMTONE_CHOICES, default='music1')
    time = models.DateTimeField(help_text='Choose a date and time for your alarm that is AFTER the current time')
    objects = AlarmManager()
    class Meta:
        ordering = ['time']

    def __str__(self):
        return f'{self.title} at {self.time}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this alarm."""
        return '/'


class AlarmTone(models.Model):
    ALARMTONE_CHOICES = (
        ('Love Story', 'Love Story'),
        ('Flower Dance', 'Flower Dance'),
        ('River Flows in You', 'River Flows in You'),
        ('Little Star', 'Little Star'),
    )
    sound = models.CharField(max_length=200, choices=ALARMTONE_CHOICES, default='Love Story')

    def __str__(self):
        return self.sound

class Datetime(models.Model):
    datetime = models.CharField(max_length=200)

    def __str__(self):
        return self.datetime