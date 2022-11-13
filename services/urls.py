from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('create-service/', views.createService, name='create-service'),
    path('update-service/<str:pk>/', views.updateService, name='update-service'),
    path('delete-service/<str:pk>/', views.deleteService, name='delete-service'),
    path('view-service/<str:pk>/', views.viewService, name='view-service'),
    path('category-list/', views.categoryList, name='category-list'),
    path('create-category/', views.createCategory, name='create-category'),
    path('update-category/<str:pk>/', views.updateCategory, name='update-category'),
    path('delete-category/<str:pk>/', views.deleteCategory, name='delete-category'),
]
