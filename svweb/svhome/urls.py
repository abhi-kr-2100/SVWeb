from django.urls import path

from . import views

app_name = 'svhome'
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/<str:country>/', views.calendar, name='calendar-tz'),
    path('study-tips/', views.study_tips, name='study-tips'),
    path('social-media/', views.social_media, name='social-media'),
    path('about/', views.about, name='about')
]