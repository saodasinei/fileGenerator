from django.urls import path
from . import views

urlpatterns = [
     path('', views.generator),
     path('generate/', views.fission),
     path('search/', views.search),
     path('savenewfile/', views.savenewfile),
     path('upload/', views.upload),
     path('upload/excel/', views.uploadexcel)
]
