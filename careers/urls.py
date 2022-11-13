from django.urls import path
from . import views

urlpatterns = [
    path('job-board/', views.jobBoard, name='job-board'),
    path('job-app-list/', views.jobAppList, name='job-app-list'),
    path('view-job-app/<str:pk>/', views.viewJobApp, name='view-job-app'),
    path('delete-app/<str:pk>/', views.deleteJobApp, name='delete-app'),
    path('apply-job/<str:jobId>/', views.applyJob, name='apply-job'),
    path('post-job/', views.postJob, name='post-job'),
    path('update-job/<str:pk>/', views.updateJob, name='update-job'),
    path('delete-job/<str:pk>/', views.deleteJob, name='delete-job'),
    
]
