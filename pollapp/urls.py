from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'pollapp'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('polls/', views.PollListView.as_view(), name='poll_list'),
    path('<int:pk>/report/', views.ReportView.as_view(), name='poll_report'),
    path('polls/<int:pk>', views.PollDetailView.as_view(), name='poll_detail'),
    path('<int:question_id>', views.vote, name='vote'),
    path('taken_polls/', views.TakenListView.as_view(), name='taken_poll_list'),




]
