from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_ind, name='index'), # url 요청에 의해 응답하는 함수 매칭을 위한 import
    path('movie-detail/', views.info, name='info'),
]