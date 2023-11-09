from django.urls import path 
from . import views 

urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
    path('create-account', views.registerUser, name='create-account'),
    path('edit-account/', views.editAccount, name='edit-account'),
	
]