from django.urls import path 
from . import views 

urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
    path('create-account', views.createAccount, name='create-account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('list-accounts/', views.listAccounts, name='list-accounts'),
	path('delete-account/<uuid:pk>/', views.deleteAccount, name='delete-account'),
    path('admin-edit-account/<uuid:pk>/', views.adminEditAccount, name='admin-edit-account'),
]