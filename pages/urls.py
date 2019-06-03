from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #view의 index를 바라봄
    path('dinner/',views.dinner),
    path('hello/<str:name>/', views.hello),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('times/<int:num_1>/<int:num_2>/', views.times),
    path('area/<int:radius>/', views.area),
]
