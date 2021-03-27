"""To_Do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Firstpage import views


#app_name += 'Signin_Logout'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('current_todo/', views.current_todo, name='current_todo'),
    path('completed_todos/', views.completed_todos, name='completed_todos'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/completed', views.completed, name='completed'),
    path('todo/<int:todo_pk>/delete', views.delete, name='delete'),
    path('logout/', views.logoutuser, name='logoutuser'),


]
