from django.urls import path
from . import views

urlpatterns = [
     path('', views.generator),
     path('generate/', views.fission),
     path('savenewfile/', views.savenewfile),
     path('checking/', views.checking),
     path('test/', views.test),
]
