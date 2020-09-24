from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.login),
     path('login/identify/', views.identify),
     path('upload/', views.upload),
     path('upload/excel/', views.uploadexcel),
     path('upload/save/', views.saveupload),
     path('upload/history/', views.history),
     path('upload/content/', views.content),
     path('manage/', views.manage)
]
