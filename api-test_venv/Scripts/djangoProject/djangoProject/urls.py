"""djangoProject URL Configuration

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
from django.urls import path
#下面這段import不加會錯
from django.urls import path, include
from django.conf.urls import url #給url參數用
#-------------------
from mysqlTest import views
#-----------------
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.user),
    url(r'^add/$', views.add), #user01.html的form action
    url(r'^getAllUser/$', views.getAllUser), #查詢所有user
]
