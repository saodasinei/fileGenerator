from django.urls import path
from . import views

urlpatterns = [
     path('', views.login),
     path('login/', views.login),
     path('login/loginAction/', views.loginAction),
     path('login/logoutAction/', views.logoutAction),
     path('upload/', views.upload),
     path('upload/excel/', views.uploadexcel),
     path('upload/save/', views.saveupload),
     path('upload/history/', views.history),
     path('upload/content/', views.content),
     path('manage/', views.manage),
     path('manage/review/', views.manage_review),
     path('manage/parttimer/', views.manage_parttimer)
]
