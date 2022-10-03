from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbv/', views.Taskview.as_view(), name='cbv'),
    path('cbvd/<int:pk>/', views.TaskDview.as_view(), name='cbvd'),
   # path('details', views.details, name='details'),
    path('cbvu/<int:pk>/', views.updatwview.as_view(), name='cbvu'),
    path('cbvde/<int:pk>/', views.Deleteview.as_view(), name='cbvde'),
]
