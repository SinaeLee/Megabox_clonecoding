from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_ind, name='index') # url 요청에 의해 응답하는 함수 매칭을 위한 import

]