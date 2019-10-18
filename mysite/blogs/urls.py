from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
     path('detail/<int:blog_id>/', views.detail, name='detail'),
      path('users/<int:pk>/', views.users_detail, name='users_detail'),
      path('signup/', views.signup, name='signup'),
     path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]