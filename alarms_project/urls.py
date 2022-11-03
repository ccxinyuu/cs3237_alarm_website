from django.urls import path
from . import views


urlpatterns = [
    path('', views.LandingPageView.as_view(), name = 'landing'),
    path('alarms',views.HomePageView.as_view(), name = 'home'),
    path('signup/',views.signup, name = 'signup'),
    path('profile/$', views.ProfileUpdate.as_view(), name = 'profile'),
    path('alarm/create/', views.AlarmCreate.as_view(), name='alarm_create'),
    path('alarm/alarmToneChange/', views.AlarmToneChange.as_view(), name='alarm_tone_change'),
    path('alarm/<int:pk>/update/', views.AlarmUpdate.as_view(), name='alarm_update'),
    path('alarm/<int:pk>/delete/', views.AlarmDelete.as_view(), name='alarm_delete'),
    path('controller/send/', views.sendsignal, name='sendsignal')
]