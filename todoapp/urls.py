from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/',views.add_task, name='add_task'),
    path('completed_task/', views.completed_task, name='completed_task'),
    path('update_task/<str:pk>/',views.update_task,name='update_task'),
    path('delete_task/<str:pk>/',views.delete_task,name='delete_task'),
    path('completed_task/<str:pk>/',views.mark_as_done,name='mark_as_done'),
]