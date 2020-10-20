from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     path('login/', views.login),
     path('login/loginAction/', views.loginAction),
     path('login/logoutAction/', views.logoutAction),
     path('upload/', views.upload),
     path('upload/excel/', views.uploadexcel),
     path('upload/save/', views.saveupload),
     path('upload/history/', views.history),
     path('upload/content/', views.content),
     path('upload/delete/', views.delete),
     path('manage/', views.manage),
     path('manage/login/', views.managerLogin),
     path('manage/review/', views.manageReview),
     path('manage/review/filter/', views.reviewFilter),
     path('manage/review/status/', views.uploadStatus),
     path('manage/review/content/', views.reviewContent),
     path('manage/review/content/status/', views.contentStatus),
     path('manage/parttimer/', views.manageParttimer),
     path('manage/parttimer/add/', views.addParttimer),
     path('manage/parttimer/update/', views.updateParttimer),
     path('manage/parttimer/delete/', views.deleteParttimer)
]
