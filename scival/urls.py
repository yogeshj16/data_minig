from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('quests', views.quests, name='quests'),
    path('crawling_process', views.crawling_process,name='crawling_process')
]