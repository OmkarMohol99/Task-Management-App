from django.urls import path
from . import views


urlpatterns = [
    path('addTask/', views.TaskManagementView.as_view({'post':'create'}), name='add-task'),
    path('getTask/', views.TaskManagementView.as_view({'get':'list'}), name='get-task'),
    path('getTask/<int:pk>/', views.TaskManagementView.as_view({'get':'retrieve'}), name='get-task'),
    path('deleteTask/<int:pk>/', views.TaskManagementView.as_view({'delete':'destroy'}), name='delete-task'),
    path('updateTask/<int:pk>/', views.TaskManagementView.as_view({'put':'update'}), name='update-task'),
]