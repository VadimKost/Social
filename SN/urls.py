"""Social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path,re_path
from SN import views


urlpatterns = [
path('',views.User_View,name='user_v'),
path('regestration/',views.reg,name='rage'),
path('dialogs/',views.Dialog_view,name='D_v'),
re_path(r'^dialog/(?P<dialog_id>\w+)/$',views.Dialog,name='dialog_2'),
path('Auth/',views.Auth,name='Auth')
]